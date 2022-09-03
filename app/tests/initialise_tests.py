import mongoengine
from models.account import Account
from webtest import TestApp
from run import app
from werkzeug.security import generate_password_hash


class Initialise:
    def init_app(self):
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = TestApp(app)
        mongoengine.disconnect("default")
        mongoengine.connect('test_db', host='mongomock://localhost', uuidRepresentation="standard")  # uuidRepresentation argument is required to avoid warning

    def create_account(self):
        password_hash = generate_password_hash("test")
        account = Account(
            email="test@test.com",
            forename="test",
            surname="test",
            password_hash=password_hash,
        )
        account.save()


