import mongoengine
from models.account import Account
from werkzeug.security import generate_password_hash
from models.profile import Profile
from config import create_app


class Initialise:
    def init_app(self):
        app = create_app()
        app.config['WTF_CSRF_ENABLED'] = False
        self.ctx = app.app_context()
        self.ctx.push()
        self.flask_app = app
        self.app = app.test_client()
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
        self.account = account
        return str(account.id)

    def create_profile(self):
        profile = Profile(
            work_email="test@hotmail.com",
            account=str(self.create_account()),
            job_title="test",
            phone="test",
            field="test",
            specialisms=["test", "test", "test", "test"],
            certifications=["test", "test"],
            education=["test"],
            working_hours="test",
            location="test",
            bio="test",
            registration="test",
            interests=["test", "test"],
            years_experience=13,
            consultation_fee="0",
            voice="Male")
        profile.save()
        self.profile = profile
        return profile


