from unittest import TestCase
from initialise_tests import Initialise
from models.profile import Profile
from models.account import Account


class ProfileTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        self.account_id = self.create_account()

    def tearDown(self):
        Account.objects().delete()
        Profile.objects().delete()

    def test_render_chat(self):
        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        self.app.post('/login/', data=credentials, follow_redirects=True)

        response = self.app.get(f"/ar2/{self.account_id}", follow_redirects=True)
        assert b"iframe.contentWindow.postMessage" in response.data

    # def test_chat(self):
    #     request = {"data": "",
    #             "session": ""}
    #
    #
    #     response = self.app.get('/start/', follow_redirects=True)
    #     print(response.data)


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



    # def test_create_session(self):
    #     credentials = {
    #         "email": "test@test.com",
    #         "password": "test"
    #     }
    #     self.app.post('/login/', data=credentials, follow_redirects=True)
    #     self.app.get(f"/ar2/{self.account_id}", follow_redirects=True)
    #
    #     response = self.app.get("/start/",
    #                             follow_redirects=True)
    #     print(response.data)

