import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()  # load Telegram credentials

def send_telegram(message: str):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        logging.warning("Telegram credentials missing, cannot send message.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        resp = requests.post(url, data={"chat_id": chat_id, "text": message})
        if resp.status_code == 200:
            logging.info("Telegram message sent successfully.")
        else:
            logging.error(f"Failed to send Telegram message: {resp.text}")
    except Exception as e:
        logging.error(f"Error sending Telegram message: {e}")
