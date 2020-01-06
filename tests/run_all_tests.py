import os
import unittest

from flask_testing import TestCase

from application import app
from application.config import basedir
from application.entities.user.user_model import User


class TestConfig(TestCase):
    def create_app(self):
        return app

    def test_secret_key(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')

    def test_database_config(self):
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'app.db'))


class TestInitialDatabaseImage(TestCase):
    def create_app(self):
        return app

    def test_fields_of_admin(self):
        admin = User.query.get(1)
        self.assertTrue(admin.first_name == "Admin's first name")


if __name__ == '__main__':
    unittest.main()
