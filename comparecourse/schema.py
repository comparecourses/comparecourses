from peewee import *
from comparecourse import app

db = PostgresqlDatabase(app.config['DATABASE'])
class Source(Model):
    name = CharField(primary_key=True)

    class Meta:
        database = db

class University(Model):
    name = CharField()

    class Meta:
        database = db

class Course(Model):
    name = CharField()
    provider = ForeignKeyField(Source, related_name='courses')
    provider_university = ForeignKeyField(University, related_name='courses')
    description = TextField()

    class Meta:
        database = db
        indexes = (
            # create a unique on from/to/date
            (('name', 'provider', 'provider_university','description'), True),

            # create a non-unique on from/to
            (('name', 'provider', 'provider_university'), False),
        )



class Teacher(Model):
    name= CharField()
    
    class Meta:
        database = db

class CourseTeacher(Model):
    teacher = ForeignKeyField(Teacher)
    course = ForeignKeyField(Course)

    class Meta:
        database = db


class Session(Model):
    course = ForeignKeyField(Course)
    startdate= DateTimeField()
    enddate= DateTimeField()
    duration= IntegerField()

    class Meta:
        database = db

class SelfStudy(Model):
    course = ForeignKeyField(Course)
    selfstudy= BooleanField()

    class Meta:
        database = db

def create_tables():
	Source.create_table(True)
	University.create_table(True)
	Course.create_table(True)
	Teacher.create_table(True)
	CourseTeacher.create_table(True)
	Session.create_table(True)
	SelfStudy.create_table(True)

