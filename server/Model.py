from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()
class Physicians(db.Model):
    __tablename__ = 'physicians'
    id = db.Column(db.Integer, primary_key=True)
    doctor_first = db.Column(db.String(250), nullable=False)
    doctor_last = db.Column(db.String(250), nullable=False)
    doctor_email = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, doctor_first,doctor_last, doctor_email):
        self.doctor_first = doctor_first
        self.doctor_last = doctor_last
        self.doctor_email = doctor_email

class PhysiciansSchema(ma.Schema):
    id = fields.Integer()
    doctor_first = fields.String(required=True)
    doctor_last = fields.String(required=True)
    doctor_email = fields.String(required=True)

class PhysicianEvents(db.Model):
    __tablename__ = 'physician_events'
    id = db.Column(db.Integer, primary_key=True)
    physicians_id = db.Column(db.Integer, db.ForeignKey('physicians.id', ondelete='CASCADE'), nullable=False)
    patient_name = db.Column(db.String(250), nullable=False)
    start_time = db.Column(db.String(250), nullable=False)
    kind = db.Column(db.String(250), nullable=False)

    def __init__(self, physicians_id,patient_name, start_time,kind):
        self.physicians_id = physicians_id
        self.patient_name = patient_name
        self.start_time = start_time
        self.kind = kind

class PhysicianEventsSchema(ma.Schema):
    id = fields.Integer()
    patient_name = fields.String(required=True)
    start_time = fields.String(required=True)
    kind = fields.String(required=True)
