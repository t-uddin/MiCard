from unittest import TestCase

from werkzeug.datastructures import FileStorage

from initialise_tests import Initialise
from models.profile import Profile
from models.account import Account
from controllers.chat_controller import render_chat
import ast
from io import BytesIO

class ProfileTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        profile = self.create_profile()
        self.account_id = profile.account.id

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


    def test_create_session(self):
        self.app.get(f"/ar2/{self.account_id}", follow_redirects=True)

        response = self.app.get("/start/", follow_redirects=True)

        assert b"session" in response.data


    def test_chat(self):
        self.app.get(f"/ar2/{self.account_id}", follow_redirects=True)

        response = self.app.get("/start/", follow_redirects=True)

        bytes = response.data
        dict_str = bytes.decode("UTF-8")
        start_response_data = ast.literal_eval(dict_str)
        session_id = start_response_data["session"]

        sample_audio = BytesIO(b'\x1aE\xdf\xa3\x9fB\x86\x81\x01B\xf7\x81\x01B\xf2\x81\x04B\xf3\x81\x08B'
                               b'\x82\x84webmB\x87\x81\x04B\x85\x81\x02\x18S\x80g\x01\xff\xff\xff\xff\xff'
                               b'\xff\xff\x15I\xa9f\x99*\xd7\xb1\x83\x0fB@M\x80\x86ChromeWA\x86Chrome\x16T'
                               b'\xaek\xbf\xae\xbd\xd7\x81\x01s\xc5\x87\x1dV!)\x7f\x01\x9a\x83\x81\x02\x86'
                               b'\x86A_OPUSc\xa2\x93OpusHead\x01\x01\x00\x00\x80\xbb\x00\x00\x00\x00\x00\xe1'
                               b'\x8d\xb5\x84G;\x80\x00\x9f\x81\x01bd\x81 \x1fC\xb6u\x01\xff\xff\xff\xff\xff'
                               b'\xff\xff\xe7\x81\x00\xa3A\xc3\x81\x00\x00\x80\xfb\x83\xe6g~0\xfc!\xfcU\x04'
                               b'\xc3\xafIc\x15H\xa9a\x17\x16[\x86l\xe0\xc0cT;\x19\xcf\x94\xfd\xc7\x98\xc6'
                               b'\xa0\xaf$\xbf\xe44\xfc\xb3+\xd8\x8e\xf0\x81\xd3~\xaf(\x88\xca\x8dW\xa5\x14}'
                               b'\xf9\xf6:\xb9\xec\x052\x18\xa7\xbdyj\xab\x8fD\xdeE}\x01h\xbd4\xd4S\xd8\x08'
                               b'\xa6V\xda"\xac\xcf\x85\x9fXA*\xe1\xbe\xc6h\xae\xe5\xa1\xb9\xd8,IT`\xa9\xab'
                               b'\x83G\xb6@\x8f\xdb\xbe\x9e\'\xc0@\xe8\x82\xe1`\x90 CFq\x1c\x9e\x03>\xe6*')


        file_storage = FileStorage(stream=sample_audio, name="data", filename="sample_query")

        chat_request_data = {
            "data": file_storage,
            "session": session_id
        }

        response = self.app.post('/chat/', data=chat_request_data, follow_redirects=True)

        assert b"audio" in response.data



