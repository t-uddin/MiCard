from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from environment import assistant_api_key, assistant_id, assistant_api_url
from controllers.profile_controller import Profile


class WatsonAssistant:
    def __init__(self):
        self.assistant_id = assistant_id
        authenticator = IAMAuthenticator(assistant_api_key)
        self.assistant_service = AssistantV2(
            version="2021-11-27",
            authenticator=authenticator
        )

        self.assistant_service.set_service_url(assistant_api_url)

    def new_session(self):
        self.response = self.assistant_service.create_session(
            assistant_id=self.assistant_id
        ).get_result()
        self.session_id = self.response.get("session_id")

        return self.session_id

    def send_message(self, text):
        response = self.assistant_service.message(
            session_id=self.session_id,
            assistant_id=self.assistant_id,
            input={
                'message_type': 'text',
                'text': text,
                'options': {'return_context': True}
            }
        ).get_result()

        answer = (response["output"]["generic"][0]["text"])
        print(answer)

        if answer:
            return answer
        else:
            return "Sorry, I did not understand, could you rephrase your question?"


    def send_context(self, profile):
        # remove Null values from being sent as context variables
        # nprofile = {k: v for k, v in profile.items() if v != None}
        input_profile = {}

        for k, v in profile.items():
            if v:
                input_profile[k] = v
                # convert list objects into natural language
                if isinstance(v, list) and len(v) > 1:
                    v.insert(-1, 'and')
                    ', '.join([str(a) for a in v])


        # set context variables to send
        context = {
            'skills': {
                'main skill': {
                    'user_defined': {
                        k: v for k, v in input_profile.items() if v
                    }
                }
            }
        }

        # set input message
        input = {
            'message_type': 'text',
            'text': "_@_Data58302"
        }

        # send
        response = self.assistant_service.message(
            session_id=self.session_id,
            assistant_id=self.assistant_id,
            input=input,
            context=context
        ).get_result()

        return None


profile = Profile.get("62e6f4e8d1d8472cf1002c40")

# hi = WatsonAssistant()
# session = hi.new_session()
# hi.send_context("Are you registered", profile)
# hi.send_with_context("how can i contact you", profile)
