import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from objects import TeacherObject, CourseObject, SchoolSubjectObject, QuestionObject, CategoryObject, OfferedAnswerObject, AnswerChoiceObject, AnswerTextObject, AnswerObject
from models import AnswerText, AnswerChoice, Question
from database import db_session

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    teacher = graphene.Field(TeacherObject, id=graphene.Int())
    def resolve_teacher(self, info, id):
        query = TeacherObject.get_query(info)
        return query.get(id)
    
    course = graphene.Field(CourseObject, id=graphene.Int())
    def resolve_course(self, info, id):
        query = CourseObject.get_query(info)
        return query.get(id)
    
    all_teacher = SQLAlchemyConnectionField(TeacherObject)
    all_course = SQLAlchemyConnectionField(CourseObject)
    all_school_subjects = SQLAlchemyConnectionField(SchoolSubjectObject)
    all_category = SQLAlchemyConnectionField(CategoryObject)
    all_question = SQLAlchemyConnectionField(QuestionObject)

class ReplyAnswerText(graphene.Mutation):
    class Arguments:
        teacher_id = graphene.Int(required=True)
        school_subject_id = graphene.Int(required=True)
        course_id = graphene.Int(required = True)
        questions_id = graphene.List(graphene.Int, required=True)
        replies = graphene.List(graphene.String, required=True)
    
    ok = graphene.Boolean()

    def mutate(self, info, teacher_id, school_subject_id, course_id, questions_id, replies):
        queryAnswersChoice = db_session.query(Question.question_id).filter_by(is_choice=True)
        queryAnswersChoice = [value for value, in queryAnswersChoice]

        for i in range(len(questions_id)):
            if questions_id[i] in queryAnswersChoice:
                answer = AnswerChoice(question_id=questions_id[i], teacher_id=teacher_id, school_subject_id=school_subject_id, course_id=course_id, offered_answer_id=int(replies[i]))
            else:
                answer = AnswerText(question_id=questions_id[i], teacher_id=teacher_id, school_subject_id=school_subject_id, course_id=course_id, reply=replies[i])
        
            db_session.add(answer)
        
        db_session.commit()
        
        ok = True
        
        return ReplyAnswerText(ok=ok)

class Mutation(graphene.ObjectType):
   reply_answer_text = ReplyAnswerText.Field()


schema = graphene.Schema(query=Query, types=[TeacherObject], mutation=Mutation)
