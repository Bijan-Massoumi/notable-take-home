from flask import Blueprint
from flask_restful import Api
from resources.Helper import PhysiciansResource, PhysicianEventsResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(PhysiciansResource, '/physicians')
api.add_resource(PhysicianEventsResource, '/physician_events')


