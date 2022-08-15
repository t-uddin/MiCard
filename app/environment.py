import os
from dotenv import load_dotenv

load_dotenv()

# IBM variables
tts_api_key = os.environ.get("TTS_API_KEY")
tts_api_url = os.environ.get("TTS_URL")

stt_api_key = os.environ.get("STT_API_KEY")
stt_api_url = os.environ.get("STT_URL")

assistant_api_key = os.environ.get("ASSISTANT_API_KEY")
assistant_api_url = os.environ.get("ASSISTANT_URL")
assistant_id = os.environ.get("ASSISTANT_ID")

# Mongo variables
mongo_host = os.environ.get("MONGO_URI")

# Flask variables
secret_key = os.environ.get("SECRET_KEY")



