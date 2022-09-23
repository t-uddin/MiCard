from unittest import TestCase
from initialise_tests import Initialise
from models.profile import Profile
from models.account import Account


class ProfileTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()

    def tearDown(self):
        Account.objects().delete()
        Profile.objects().delete()

    def test_get_create_profile(self):
        self.create_account()
        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        self.app.post('/login/', data=credentials, follow_redirects=True)

        profile = {
            "new_bio": "test",
            "new_email": "test2@hotmail.com",
            "new_title": "test",
            "new_phone": "test",
            "new_hours": "test",
            "new_location": "test",
            "new_field": "test",
            "new_registration": "test",
            "new_years": 10,
            "new_fee": "0",
            "new_specialisms": ["test"],
            "new_treatments": ["test"],
            "new_certifications": ["test"],
            "new_education": ["test"],
            "new_interests": ["test"]
        }

        response = self.app.post('/profile-create/', data=profile,
                                 follow_redirects=True)
        assert b"test" in response.data

    def test_get_edit_profile(self):
        self.create_profile()

        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        self.app.post('/login/', data=credentials, follow_redirects=True)

        profile = {
            "new_bio": "updated bio",
            "new_email": "test2@hotmail.com",
            "new_title": "test",
            "new_phone": "test",
            "new_hours": "test",
            "new_location": "test",
            "new_field": "test",
            "new_registration": "test",
            "new_years": 10,
            "new_fee": "0",
            "new_specialisms": ["test"],
            "new_treatments": ["test"],
            "new_certifications": ["test"],
            "new_education": ["test"],
            "new_interests": ["test"]
        }

        response = self.app.post('/profile-edit/', data=profile,
                                 follow_redirects=True)
        assert b"updated bio" in response.data

    def test_get_register_profile(self):
        # TODO
        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        self.app.post('/login/', data=credentials, follow_redirects=True)

        data = dict(
            specialisms=["test"],
            treatments=["test"],
            certifications=["test"],
            education=["test"],
            interests=["test"],
        )

        response = self.app.post('/profile-register/', data=data,
                                 follow_redirects=True)

        # print(response.data)