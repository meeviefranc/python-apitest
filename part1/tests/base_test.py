"""
BaseTest
parent class for each non-unit test to allow instantiation of the db dynamically
and make sure it is a new blank db on each test execution.
"""

from unittest import TestCase
from part1.app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # make sure db exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            # db.init_app(app.app)
            db.init_app(app)
            db.create_all()
        # get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # db is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
