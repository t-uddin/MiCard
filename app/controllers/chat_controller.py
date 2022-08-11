from models.watson import WatsonAssistant
from controllers.profile_controller import Profile
from models.tts import Speak
from models.stt import Transcribe


def converse(cardid):
    '''start dialog loop with Watson'''
    assistant = WatsonAssistant()
    session = assistant.new_session()
    profile = Profile.get(cardid)

    # first send card profile data as context variables
    resp = assistant.send_context(profile)
    print(resp)

    print ("Starting a conversation, stop by Ctrl+C or saying 'bye'")
    print ("======================================================")

    while True:
        # get user input text
        # text = input("\nEnter your input message:\n")
        text = Transcribe().transcribe_live_audio()
        print(text)

        # Send the session context on first iteration of the loop
        print("entered")

        resp = assistant.send_message(text)
        print(resp)
        Speak().text_to_audio(resp, "male")

        # Save returned context for next round of conversation
        if ('context' in resp):
            context = resp['context']


# Testing -------------------------------------------
if __name__ == '__main__':
    cardid = "62e6f4e8d1d8472cf1002c40"
    converse(cardid)