from unittest import TestCase
from initialise_tests import Initialise
from models.account import Account



class AuthTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        self.create_account()

    def tearDown(self):
        pass

    def test_valid_login(self):
        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        response = self.app.post('/login/', data=credentials, follow_redirects=True)
        assert b"Welcome test" in response.data

    def test_invalid_login(self):
        credentials = {
            "email": "fake_user@test.com",
            "password": "test"
        }
        response = self.app.post('/login/', data=credentials, follow_redirects=True)
        assert b"There is no account with this email/password combination." in response.data

    def test_not_matching_password_registration(self):
        signup_info = {
            "email": "new_user@test.com",
            "forename": "Test",
            "surname": "Test",
            "password": "test_password",
            "confirm_psw": "Test",
        }
        response = self.app.post('/register/', data=signup_info, follow_redirects=True)
        assert b"Passwords do not match" in response.data

    def test_existing_email_registration(self):
        signup_info = {
            "email": "test@test.com",
            "forename": "Test",
            "surname": "Test",
            "password": "test_password",
            "confirm_psw": "test_password",
        }
        response = self.app.post('/register/', data=signup_info, follow_redirects=True)
        assert b"An account already exists with this email" in response.data

    def test_valid_registration(self):
        signup_info = {
            "email": "new_test_user@test.com",
            "forename": "Test",
            "surname": "Test",
            "password": "test_password",
            "confirm_psw": "test_password",
        }
        response = self.app.post('/register/', data=signup_info, follow_redirects=True)
        assert b"Thanks for registering!" in response.data

    def test_id_get(self):
        profile = self.create_profile()
        new_id = str(profile.account.id)
        account = Account.id_get(new_id)
        response_id = str(account.get("id"))

        self.assertEqual(new_id, response_id)
