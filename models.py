from sqlalchemy import Column, Integer, ForeignKey, Table, DateTime, String, func
from sqlalchemy.orm import relationship, backref
from database import Base, engine

courseSchoolSubject = Table('course_school_subject',
                            Base.metadata,
                            Column('course_id', Integer, ForeignKey(
                                'course.course_id'), primary_key=True),
                            Column('school_subject_id', Integer, ForeignKey(
                                'school_subject.school_subject_id'), primary_key=True)
                            )


class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True)
    schools_subjects = relationship(
        'SchoolSubject', secondary=courseSchoolSubject, backref=backref('courses', lazy='dynamic'))
    answersText = relationship('AnswerText', backref='course', lazy=True)
    answersChoice = relationship('AnswerChoice', backref='course', lazy=True)

teacherSchoolSubject = Table('teacher_school_subject',
                             Base.metadata,
                             Column('teacher_id', Integer, ForeignKey(
                                 'teacher.teacher_id'), primary_key=True),
                             Column('school_subject_id', Integer, ForeignKey(
                                 'school_subject.school_subject_id'), primary_key=True)
                             )


class SchoolSubject(Base):
    __tablename__ = 'school_subject'

    school_subject_id = Column(Integer, primary_key=True)
    teachers = relationship('Teacher', secondary=teacherSchoolSubject, backref=backref(
        'schools_subjects', lazy=True))
    answersText = relationship('AnswerText', backref='school_subject', lazy=True)
    answersChoice = relationship('AnswerChoice', backref='school_subject', lazy=True)

class Teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column(Integer, primary_key=True)
    answersText = relationship('AnswerText', backref='teacher', lazy=True)
    answersChoice = relationship('AnswerChoice', backref='teacher', lazy=True)


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    questions = relationship('Question', backref='category', lazy=True)


questionOfferedAnwser = Table('question_offered_answer',
                              Base.metadata,
                              Column('question_id', Integer, ForeignKey(
                                  'question.question_id'), primary_key=True),
                              Column('offered_answer_id', Integer, ForeignKey(
                                  'offered_answer.offered_answer_id'), primary_key=True)
                              )


class Question(Base):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'),
                         nullable=False)
    offeredAnswers = relationship(
        'OfferedAnswer', secondary=questionOfferedAnwser, backref=backref('questions', lazy='dynamic'))
    answersText = relationship('AnswerText', backref='question', lazy=True)
    answersChoice = relationship('AnswerChoice', backref='question', lazy=True)


class OfferedAnswer(Base):
    __tablename__ = 'offered_answer'

    offered_answer_id = Column(Integer, primary_key=True)


class Answer(Base):
    __tablename__ = 'answer'

    answer_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey(
        'question.question_id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey(
        'teacher.teacher_id'), nullable=False)
    school_subject_id = Column(Integer, ForeignKey(
        'school_subject.school_subject_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    date_answer = Column(DateTime, default=func.now())
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'answer',
        'polymorphic_on':type
    }

class AnswerText(Answer):
    __tablename__ = 'answer_text'
    
    answer_id = Column(Integer, ForeignKey('answer.answer_id'), primary_key=True)
    reply = Column(String, nullable=False)

    __mapper_args__ = {'polymorphic_identity':'answerText'}


class AnswerChoice(Answer):
    __tablename__ = 'answer_choice'
    
    answer_id = Column(Integer,ForeignKey('answer.answer_id'), primary_key=True)    
    offered_answer_id = Column(Integer, ForeignKey(
        'offered_answer.offered_answer_id'), primary_key=True)
    
    __mapper_args__ = {'polymorphic_identity':'answerChoice'}

Base.prepare(engine)
