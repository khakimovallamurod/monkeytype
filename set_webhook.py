import requests
import os
from telegram import Bot
from html2image import Html2Image

TOKEN = os.environ['TOKEN']
WEBHOOK_URL = f"https://allamurod.pythonanywhere.com/"

response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(response.status_code)
bot = Bot(TOKEN)
bot.delete_webhook()

