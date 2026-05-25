import requests
from config import TELEGRAM_BOT_TOKEN

def send_telegram_message(chat_id, text):

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, data=data)

    print("텔레그램 응답:")
    print(response.status_code)
    print(response.text)