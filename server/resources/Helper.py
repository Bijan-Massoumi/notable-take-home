from flask import request
import json
from flask_restful import Resource
from Model import db, Physicians, PhysicianEvents, PhysicianEventsSchema, PhysiciansSchema



physicians_schema = PhysiciansSchema(many=True)
physician_schema = PhysiciansSchema()
class PhysiciansResource(Resource):
    def get(self):
        doctors = Physicians.query.all()
        doctors = physicians_schema.dump(doctors).data
        return {'status': 'success', 'data': doctors}, 200

physician_events_schema = PhysicianEventsSchema(many=True)
class PhysicianEventsResource(Resource):
    def get(self):
        
        id = request.args.get('id')
        if not id:
            return {'message': 'No input data provided'}, 400

        events = PhysicianEvents.query.filter_by(physicians_id=id).all()
        events = physician_events_schema.dumps(events).data
        return {'status': 'success', 'data': events}, 200


