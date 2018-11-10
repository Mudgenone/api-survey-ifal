import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from objects import TeacherObject, CourseObject, SchoolSubjectObject, QuestionObject, CategoryObject, OfferedAnswerObject, AnswerObject, AnswerChoiceObject, AnswerTextObject


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


schema = graphene.Schema(query=Query, types=[TeacherObject])
