import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Course, SchoolSubject, Teacher, Category, Question, OfferedAnswer, Answer, AnswerText, AnswerChoice


class TeacherObject(SQLAlchemyObjectType):
    class Meta:
        model = Teacher
        interfaces = (relay.Node, )


class CourseObject(SQLAlchemyObjectType):
    class Meta:
        model = Course
        interfaces = (relay.Node, )


class SchoolSubjectObject(SQLAlchemyObjectType):
    class Meta:
        model = SchoolSubject
        interfaces = (relay.Node, )


class CategoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node, )


class QuestionObject(SQLAlchemyObjectType):
    class Meta:
        model = Question
        interfaces = (relay.Node, )


class OfferedAnswerObject(SQLAlchemyObjectType):
    class Meta:
        model = OfferedAnswer
        interfaces = (relay.Node, )


class AnswerObject(SQLAlchemyObjectType):
    class Meta:
        model = Answer
        interfaces = (relay.Node, )


class AnswerTextObject(SQLAlchemyObjectType):
    class Meta:
        model = AnswerText
        interfaces = (relay.Node, )


class AnswerChoiceObject(SQLAlchemyObjectType):
    class Meta:
        model = AnswerChoice
        interfaces = (relay.Node, )
