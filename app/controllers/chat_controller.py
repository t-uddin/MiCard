from models.watson import WatsonAssistant
from models.profile import Profile
from models.account import Account
from models.tts import Speak
# from models.stt import Transcribe
from models.stt_new import SpeechToText
from flask import render_template, redirect, request, flash, Blueprint, url_for, jsonify
import os

chat_bp = Blueprint('chat_bp', __name__)



@chat_bp.route('/ar2/<account_id>/', methods=["GET"])
def render_chat(account_id):
    global card_id
    card_id = account_id
    return card_id, render_template('ar-iframe.html')


@chat_bp.route('/start/', methods=["GET"])
def create_session():
    # get card profile data
    print(card_id)
    profile = Profile.get(card_id)
    avatar_id = profile['avatar_id']

    global voice
    voice = profile['voice']

    account = Account.id_get(card_id)
    print(account)
    account_name = (account['forename'] + " " + account['surname'])


    # account = Account.get(profile.ac)
    # account_name = Account
    print(profile)

    # set up new watson assistant session
    card_assistant = WatsonAssistant()
    session = card_assistant.new_session()

    # send card profile data as context variables to session
    card_assistant.send_context(profile, session)
    WatsonAssistant.assistants[card_id] = card_assistant
    print(card_assistant)
    print(session)

    # send required data to AR app
    profile = {
        'session': session,
        'account_name': account_name,
        'avatar_id': avatar_id,
        'card_id': card_id
    }

    return jsonify(profile)  # serialize and use JSON headers


# I can just send the avatar and voice and name here ????


@chat_bp.route('/audio/', methods=['POST'])
def process_input():
    # transcribe users input
    print("message received")
    input_data = request.files["data"]
    session = request.form['session']
    # card_id = "62e6f4e8d1d8472cf1002c40"

    text = SpeechToText().transcribe(input_data)

    # get response from Watson Assistant
    resp = WatsonAssistant().send_message(text, session)
    print("response: ", resp)

    print("voice: ", voice)
    timestamp = Speak().text_to_audio(resp, voice, session)
    sound_path = session + timestamp

    return sound_path


@chat_bp.route('/clearaudio/', methods=['POST'])
def clear_audio():
    print("clear audio input:", request.form['id'])

    audio_path = "static/audio/" + str(request.form['id']) + ".mp3"

    if os.path.exists(audio_path):
        os.remove(audio_path)
        print("deleted")
        return "Deleted"
    else:
        print("not deleted")
        return "No audio"



# @chat_bp.route('/chat/', methods=["GET"])
# def converse():
#     cardid = "62e6f4e8d1d8472cf1002c40"
#     '''start dialog loop with Watson'''
#     assistant = WatsonAssistant()
#     session = assistant.new_session()
#     profile = Profile.get(cardid)
#     print(profile)
#
#     # first send card profile data as context variables
#     resp = assistant.send_context(profile)
#     print(resp)
#
#     print("Starting a conversation, stop by Ctrl+C or saying 'bye'")
#     print("======================================================")
#
#     while True:
#         # get user input text
#         text = input("\nEnter your input message:\n")
#         text = Transcribe().transcribe_live_audio()
#         print(text)
#
#         # Send the session context on first iteration of the loop
#         print("entered")
#
#         resp = assistant.send_message(text)
#         print(resp)
#         # Speak().text_to_audio(resp, "male")
#
#         # Save returned context for next round of conversation
#         if ('context' in resp):
#             context = resp['context']

# if __name__ == '__main__':
#     cardid = "62e6f4e8d1d8472cf1002c40"
#     converse()
