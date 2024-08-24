import requests
import os

TOKEN = os.environ['TOKEN']
WEBHOOK_URL = f"https://allamurod.pythonanywhere.com/"

# Set webhook
response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(response.status_code)