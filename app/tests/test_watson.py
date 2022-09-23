from unittest import TestCase
from initialise_tests import Initialise
from models.watson import WatsonAssistant


class WatsonTest(TestCase, Initialise):
    def setUp(self):
        self.assistant = WatsonAssistant()
        self.session_id = self.assistant.new_session()
        self.create_profile()

    def tearDown(self):
        pass

    def test_watson_chat(self):
        msg = self.assistant.send_message("what are your  hours", self.session_id)
        self.assertEqual(msg, "My working hours are ")

    def test_watson_context(self):
        msg = self.assistant.send_context(self.profile.to_dict(), self.assistant.session_id)
        self.assertIsNone(msg)
