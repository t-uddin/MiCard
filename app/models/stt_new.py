from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from environment import stt_api_key, stt_api_url


class SpeechToText:
    def __init__(self):
        '''Initialise and setup speech to text'''
        authenticator = IAMAuthenticator(stt_api_key)
        self.speech_to_text = SpeechToTextV1(
            authenticator=authenticator
        )
        self.speech_to_text.set_service_url(stt_api_url)

    def transcribe(self, audio_file):
        speech_recognition_results = self.speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/webm',
            model='en-GB_Telephony',
            inactivity_timeout=10
        ).get_result()

        try:
            text = speech_recognition_results['results'][0]["alternatives"][0]["transcript"]

        except Exception:
            text = ""

        finally:
            return text
