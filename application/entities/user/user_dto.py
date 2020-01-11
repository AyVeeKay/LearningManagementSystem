from flask_restplus import fields, Namespace


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model("user", {
        "public_id": fields.String(required=True, description="user's ID"),
        "password": fields.String(required=True, description="user's password"),

        "first_name": fields.String(required=True, description="user's name"),
        "middle_name": fields.String(description="user's middle name"),
        "last_name": fields.String(required=True, description="user's family name"),

        "email": fields.String(required=True, description="user's e-mail address"),
        "registered_on": fields.DateTime(required=True, description="user's datetime registered on"),
        "admin": fields.String(required=True, description="flag, that user has admin permissions"),
    })
