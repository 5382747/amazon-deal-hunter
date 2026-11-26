import os
import json
import urllib.request

def send_telegram_message(message):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = json.dumps({
        "chat_id": chat_id,
        "text": message
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        print(response.read().decode("utf-8"))

if __name__ == "__main__":
    send_telegram_message(
        "Amazon Deal Hunter: collegamento Telegram verificato!"
    )
