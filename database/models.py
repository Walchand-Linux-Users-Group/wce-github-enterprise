from mongoengine import *


class Batch(Document):
    id = LongField(unique=True)
    departments = ListField(ReferenceField(Department))


class Department(Document):
    id = LongField(unique=True)
    semesters = ListField(ReferenceField(Batch))


class Semester(Document):
    id = LongField(unique=True)
    teams = ListField(ReferenceField(Teams))


class Team(Document):
    id = LongField(unique=True)
    users = ListField(ReferenceField(User))


class User(Document):
    username = StringField()
    moodleId = LongField(unique=True)
    teams = ListField(ReferenceField(Team))
