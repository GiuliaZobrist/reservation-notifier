import requests
import os
from bs4 import BeautifulSoup
import logging
from dotenv import load_dotenv

load_dotenv()


def check_reservation(url: str) -> bool:
    """
    Return True if 'TRIGGER_WORD' appears on the page text.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Request failed for {url}: {e}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    return os.getenv("TRIGGER_WORD") in soup.get_text().lower()
