import os
from dotenv import load_dotenv

load_dotenv()

tts_api_key = os.environ.get("TTS_API_KEY")
tts_api_url = os.environ.get("TTS_URL")

stt_api_key = os.environ.get("STT_API_KEY")
stt_api_url = os.environ.get("STT_URL")

mongo_host = os.environ.get("MONGO_URI")

secret_key = os.environ.get("SECRET_KEY")