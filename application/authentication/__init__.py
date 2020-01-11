from flask import request
from flask_httpauth import HTTPBasicAuth


class HTTPEmailPassAuth(HTTPBasicAuth):
    def email(self):
        if not request.authorization:
            return ""
        return request.authorization.username


auth = HTTPEmailPassAuth()

from .authentication_service import AuthService


@auth.verify_password
def verify_pw(email, password):
    return AuthService.check_email_password_pair(email, password)
