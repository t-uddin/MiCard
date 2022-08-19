from models.watson import WatsonAssistant
from controllers.profile_controller import Profile
from models.tts import Speak
# from models.stt import Transcribe
from models.stt_new import SpeechToText
from flask import render_template, redirect, request, flash, Blueprint, url_for
import threading
import time
from flask import Flask, Response, render_template
import os

chat_bp = Blueprint('chat_bp', __name__)


# assistants = {}

@chat_bp.route('/ar2/<account_id>/', methods=["GET"])
def render_chat(account_id):
    card_id = account_id

    # start a thread
    # t = threading.Thread(target=converse(cardid))
    # t.daemon = True         # Daemonize
    # t.start()

    # t2 = threading.Thread(target=render_template('ar-iframe.html', id=cardid))
    # t2.start()

    # send data to Watson Assistant
    card_assistant = WatsonAssistant()
    session = card_assistant.new_session()
    profile = Profile.get(card_id)
    print(profile)

    # first send card profile data as context variables
    card_assistant.send_context(profile)
    WatsonAssistant.assistants[card_id] = card_assistant
    print(card_assistant)

    return render_template('ar-iframe.html')


@chat_bp.route('/chat/', methods=["GET"])
def converse():
    cardid = "62e6f4e8d1d8472cf1002c40"
    '''start dialog loop with Watson'''
    assistant = WatsonAssistant()
    session = assistant.new_session()
    profile = Profile.get(cardid)
    print(profile)

    # first send card profile data as context variables
    resp = assistant.send_context(profile)
    print(resp)

    print("Starting a conversation, stop by Ctrl+C or saying 'bye'")
    print("======================================================")

    while True:
        # get user input text
        # text = input("\nEnter your input message:\n")
        text = Transcribe().transcribe_live_audio()
        print(text)

        # Send the session context on first iteration of the loop
        print("entered")

        resp = assistant.send_message(text)
        print(resp)
        # Speak().text_to_audio(resp, "male")

        # Save returned context for next round of conversation
        if ('context' in resp):
            context = resp['context']


# @chat_bp.route('/audio')
# def audio():
#     # start Recording
#     def sound():
#         CHUNK = 1024
#         sampleRate = 44100
#         bitsPerSample = 16
#         channels = 1
#         wav_header = genHeader(sampleRate, bitsPerSample, channels)
#
#         stream = audio1.open(format=FORMAT, channels=1,
#                              rate=RATE, input=True, input_device_index=1,
#                              frames_per_buffer=CHUNK)
#         print("recording...")
#         # frames = []
#         first_run = True
#         while True:
#             if first_run:
#                 data = wav_header + stream.read(CHUNK)
#                 first_run = False
#             else:
#                 data = stream.read(CHUNK)
#             yield (data)
#
#     return Response(sound())
#

# Testing ---------------------------------------------------------------------------------



@chat_bp.route('/audio/', methods=['POST'])
def process_input():
    # transcribe users input
    print("message received")
    print(request.files["data"])
    print(request.form['id'])

    text = SpeechToText().transcribe(request.files["data"])

    # get response from Watson Assistant
    card_id = "62e6f4e8d1d8472cf1002c40"
    # print(WatsonAssistant.assistants)

    assistant = WatsonAssistant.assistants[card_id]
    print(assistant)

    # first send card profile data as context variables
    resp = assistant.send_message(text)
    print("response: ", resp)

    timestamp = Speak().text_to_audio(resp, "male")
    session = "session"
    # print("transcribed object:", speech)
    # sound = bytearray(speech)
    sound_path = session + timestamp
    return sound_path


@chat_bp.route('/clearaudio/', methods=['POST'])
def clear_audio():
    print("clear audio input:", request.form['id'])
    audio_path = "app/static/audio/" + str(request.form['id']) + ".mp3"

    if os.path.exists(audio_path):
        os.remove(audio_path)
        print("deleted")
        return "Deleted"
    else:
        print("not deleted")
        return "No audio"



if __name__ == '__main__':
    cardid = "62e6f4e8d1d8472cf1002c40"
    converse()
