from datetime import time, timezone, date
from . import db
import enum


class GenderEnum(enum.Enum):
    male = "M"
    female = "F"


class NotifyEnum(enum.Enum):
    yes = "Y"
    N = "N"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(100))
    gender = db.Column(enum.Enum(GenderEnum))
    birthdate = db.Column(db.Date(timezone=True))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    id_profession = db.Column(db.Integer, db.ForeignKey('profession.id'))
    password = db.Column(db.String(256))
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))


class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profession = db.Column(db.String(50))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_title = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))


class SubTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_task = db.Column(db.Integer, db.ForeignKey('task.id'))
    subtask = db.Column(db.String(255))
    notify = db.Column(enum.Enum(NotifyEnum))
    time = db.Column(db.Time(timezone=True))


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(255))
    cash_in = db.Column(db.Integer)
    total = db.Column(db.Integer)


class Outcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(255))
    cash_out = db.Column(db.Integer)
    total = db.Column(db.Integer)


class OutInFlows(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_income = db.Column(db.Integer, db.ForeignKey('income.id'))
    id_outcome = db.Column(db.Integer, db.ForeignKey('outcome.id'))
