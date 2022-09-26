from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from environment import tts_api_key, tts_api_url
from playsound import playsound
import os
from datetime import datetime


class Speak:
    # Setup Service
    def __init__(self):
        authenticator = IAMAuthenticator(tts_api_key)
        self.tts = TextToSpeechV1(authenticator=authenticator)
        self.tts.set_service_url(tts_api_url)

    def text_to_audio(self, text, gender, session):
        voice_gender = {"male": "en-GB_JamesV3Voice",
                        "female": "en-GB_CharlotteV3Voice"
                        }

        # Convert with a basic language model
        time = str(datetime.now().time())
        url = "static/audio/" + session + time + ".mp3"
        with open(url, 'wb') as input_file:
            res = self.tts.synthesize(text, accept='audio/mp3', voice=voice_gender[gender]).get_result()
            input_file.write(res.content)

        return time


# if __name__ == "__main__":
#     Speak().text_to_audio("hello", "male")