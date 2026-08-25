#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "39946374"))
API_HASH = environ.get("API_HASH", "7fdea3171ea895e2f9f15f22ff71207c")
BOT_TOKEN = environ.get("BOT_TOKEN", "8896836032:AAFhueJ-DxAiY55ya2JV0PM-4jprVQ9ujsc")

OWNER = int(environ.get("OWNER", "8417906815"))
CREDIT = environ.get("CREDIT", "")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8417906815').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8417906815').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


