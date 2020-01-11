from flask_restplus import Api
from flask import Blueprint
from application.entities.user.user_controller import api as user_api
from application.authentication.authentication_controller import api as auth_api


blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    title="LMS FLASK RESTPLUS API",
    version="0.1",
    description="Learning management system service"
)

api.add_namespace(user_api, path="/user")
api.add_namespace(auth_api, path="/login")
