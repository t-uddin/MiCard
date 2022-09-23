from models.watson import WatsonAssistant
from models.profile import Profile
from models.account import Account
from models.tts import Speak
from models.stt_new import SpeechToText
from flask import render_template, redirect, request, flash, Blueprint, url_for, jsonify
import os

chat_bp = Blueprint('chat_bp', __name__)


@chat_bp.route('/ar2/<account_id>/', methods=["GET"])
def render_chat(account_id):
    global card_id
    card_id = account_id
    return render_template('ar-iframe.html')


@chat_bp.route('/start/', methods=["GET"])
def create_session():
    # get card profile data
    print(card_id)
    profile = Profile.get(card_id)
    avatar_id = profile['avatar_id']

    global voice
    voice = profile['voice']

    global email
    email = profile['contact_email']

    # convert lists to natural-language strings
    profile['specialisms'] = Profile.format_list(profile['specialisms'])
    profile['certifications'] = Profile.format_list(profile['certifications'])
    profile['education'] = Profile.format_list(profile['education'])
    profile['interests'] = Profile.format_list(profile['interests'])
    profile['treatments'] = Profile.format_list(profile['treatments'])

    # get card account data
    account = Account.id_get(card_id)
    account_name = (account['forename'] + " " + account['surname'])

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


@chat_bp.route('/chat/', methods=['POST'])
def process_input():
    input_data = request.files["data"]
    session = request.form['session']

    # transcribe users input
    text = SpeechToText().transcribe(input_data)

    # get response from Watson Assistant
    resp = WatsonAssistant().send_message(text, session)
    print("response: ", resp)

    # if email requested trigger email app opening
    send_email = None

    if resp == "send":
        resp = "Sure, I'll open up an email to me on your phone."
        send_email = email

    print("voice: ", voice)
    timestamp = Speak().text_to_audio(resp, voice, session)
    sound_path = session + timestamp

    data = {"audio": sound_path, "email": send_email}

    return data


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


# if __name__ == '__main__':
#     cardid = "62e6f4e8d1d8472cf1002c40"
#     converse()
