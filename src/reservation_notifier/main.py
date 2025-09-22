import json
import time
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import os

from reservation_notifier.checker import check_reservation
from reservation_notifier.notifier import send_telegram

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# -------------------------
# Load URLs from config
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
URL_FILE = BASE_DIR / "config" / "urls.json"

try:
    with open(URL_FILE, "r", encoding="utf-8") as f:
        LOCATIONS = json.load(f)["locations"]
except Exception as e:
    logging.error(f"Failed to load URL config: {e}")
    LOCATIONS = []

if not LOCATIONS:
    logging.warning("No locations found in config. Exiting.")
    exit(1)

# -------------------------
# Track last known reservation status
# -------------------------
last_status = {loc["url"]: False for loc in LOCATIONS}


# -------------------------
# Main loop
# -------------------------
def run():
    logging.info("Starting Reservation Notifier...")

    while True:
        now = datetime.now()
        # Only check between 6:00 and 22:00
        if 6 <= now.hour <= 22:
            logging.info("Checking reservation sites...")
            for loc in LOCATIONS:
                name = loc.get("name", "Unknown")
                url = loc.get("url")
                description = loc.get("description")  # optional
                if not url:
                    continue

                try:
                    available = check_reservation(url)
                    # Send notification only if status changed to available
                    if available and not last_status[url]:
                        message = f"Reservation open for {name}!"
                        if description:
                            message += f" ({description})"
                        message += f" {url}"
                        logging.info(f"Sending notification: {message}")
                        send_telegram(message)
                    last_status[url] = available
                    logging.info(f"Status for {name}: {'open' if available else 'closed'}")
                except Exception as e:
                    logging.error(f"Error checking {name}: {e}")
        else:
            logging.info("Outside of release hours (6:00-22:00). Sleeping...")

        time.sleep(CHECK_INTERVAL)


# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    run()
