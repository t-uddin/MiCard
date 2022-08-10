import pyaudio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from environment import stt_api_key, stt_api_url
from queue import Queue, Full


# define callback for the speech to text service
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)
        self.inactivity = False

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))
        self.inactivity = True

    def on_listening(self):
        print('Service is listening')

    def on_data(self, data):
        self.data = data

    def on_close(self):
        print("Connection closed")


class SpeechToText:

    def __init__(self):
        '''Initialise and setup speech to text'''
        self.CHUNK = 1024
        self.BUFF_MAX_SIZE = self.CHUNK * 10
        self.q = Queue(maxsize=int(round(self.BUFF_MAX_SIZE / self.CHUNK)))

        authenticator = IAMAuthenticator(stt_api_key)
        self.speech_to_text = SpeechToTextV1(
            authenticator=authenticator
        )
        self.speech_to_text.set_service_url(stt_api_url)
        self.websocket_callback = MyRecognizeCallback()

    def pyaudio_callback(self, in_data, frame_count, time_info, status):
        try:
            self.q.put(in_data)
        except Full:
            pass  # discard
        return None, pyaudio.paContinue

    def recognise(self, audio_source):
        # initialize speech to text service
        response = self.speech_to_text.recognize_using_websocket(audio=audio_source,
                                                                 content_type='audio/l16; rate=44100',
                                                                 recognize_callback=self.websocket_callback,
                                                                 interim_results=True,
                                                                 background_audio_suppression=0.5,
                                                                 inactivity_timeout=2,
                                                                 model="en-GB_BroadbandModel"
                                                                 )
        return response

    def transcribe_live_audio(self):
        # instantiate pyaudio
        self.audio = pyaudio.PyAudio()

        # open stream using callback
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=self.CHUNK,
            stream_callback=self.pyaudio_callback,
            start=False
        )

        self.stream.start_stream()
        audio_source = AudioSource(self.q, True, True)
        self.recognise(audio_source)

        while not self.websocket_callback.inactivity:
            pass

        # stop recording
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        audio_source.completed_recording()

        try:
            text_string = self.websocket_callback.data['results'][0]["alternatives"][0]["transcript"]

        except TypeError:
            text_string = ""

        return text_string


# print(SpeechToText().transcribe_live_audio())
