from dotenv import load_dotenv
import os

load_dotenv()

ASTROLOGER_API_KEY = os.getenv('ASTROLOGER_API_KEY')
ASTROLOGER_BASE_URL = os.getenv('ASTROLOGER_BASE_URL')