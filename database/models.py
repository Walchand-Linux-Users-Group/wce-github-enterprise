from subprocess import CompletedProcess
from mongoengine import *


class User(Document):
    fullname = StringField()
    username = StringField()
    moodleId = LongField(unique=True)
    githubId = LongField(unique=True)
    meta = {"allow_inheritance": True}


class Repository(Document):
    id = LongField(unique=True)


class Team(Document):
    id = LongField(unique=True)
    users = ListField(ReferenceField(User))
    repository = ReferenceField(Repository)


class Semester(Document):
    fullname = StringField()
    id = LongField(unique=True)
    teams = ListField(ReferenceField(Team))


class Guide(User):
    semesters = ListField(ReferenceField(Semester))
    verified = BooleanField(default=False)


class Batch(Document):
    name = StringField()
    id = LongField(unique=True)
    guides = ListField(ReferenceField(Guide))


class Department(Document):
    name = StringField()
    id = LongField(unique=True)
    batches = ListField(ReferenceField(Batch))
