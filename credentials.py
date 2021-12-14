from dotenv import load_dotenv
import os

load_dotenv('.env')

CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")
TOKEN = os.getenv("token")
