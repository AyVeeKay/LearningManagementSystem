import os
import unittest

from flask_testing import TestCase

from application.config import basedir
from application import app


class TestConfig(TestCase):
    def create_app(self):
        return app

    def test_secret_key(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')

    def test_database_config(self):
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'app.db'))


if __name__ == '__main__':
    unittest.main()
