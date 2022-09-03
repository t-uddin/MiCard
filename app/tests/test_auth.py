from unittest import TestCase
from initialise_tests import Initialise
from models.account import Account


class AuthTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        self.create_account()

    def tearDown(self):
        pass

    def test_login(self):
        print(Account.objects.first().to_dict())
        credentials = {
            "email": "test@test.com",
            "password": "test"
        }
        response = self.app.post('/login/', credentials)
        self.assertIsNone(response.mustcontain("Welcome test"))
