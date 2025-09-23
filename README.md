# 📢 Website Change Notifier

A lightweight Python project that **scrapes a website** and **sends notifications** when changes are detected.  
Originally built for signup to ``openhouse-zuerich.ch`` with notification delivery via **Telegram Bot**.

---

## 🚀 Quick Start

1. **Clone and install dependencies**
   ```bash
   git clone https://github.com/your-username/reservation-notifier.git
   cd reservation-notifier
   poetry install
   ```
2. **Configure webpages to watch**
    In folder ``config`` modify file ``urls.json`` with the urls you want to watch and scrape.

3. **Set up a Telegram Bot**
   - Create a bot with [@BotFather](https://t.me/botfather) → get your **`TELEGRAM_TOKEN`**.  
   - Find your **Chat ID** by visiting:  
     ```
     https://api.telegram.org/bot<TELEGRAM_TOKEN>/getUpdates
     ```
   - Test the bot via ``poetry run python run send_test_telegram.py`` 

4. **Create a .env file**
    In main folder rename ``.env_template``to ``.env`` and modify this content:
    ```
    TELEGRAM_TOKEN=your_token_here
    CHAT_ID=your_chat_id_here
    TRIGGER_WORD=your_word_to_scrape_here
    ```
5. **Run the checker and notifier**
    ``poetry run python src/reservation_notifier/main.py``

## 📝 Project Features & MVP Tracker

### 🟢 MVP Features
| Feature              | Description                       | Priority | Tech Notes      |
|----------------------|-----------------------------------|----------|-----------------|
| Web scraper          | Detect when a website changes.   | High     | `BeautifulSoup` |
| Telegram notification| Send alerts to Telegram chat.    | High     | `requests`      |

---

### 🟡 Nice-to-Have Extensions
| Feature               | Description                          | Impact | Effort | Notes                  |
|------------------------|--------------------------------------|--------|--------|------------------------|
| Email notifications    | Alternative to Telegram             | Medium | Low    | Risks email security   |
| Private channel alerts | Push updates to a Telegram channel  | Medium | Low    | Reliable mobile alerts |
| Automatic sign-in      | Scrape behind login pages            | High   | High   | Needs session handling |
| Status tracker         | Notify only when state changes       | High   | Medium | Add in `main.py`       |
| Service, cron          | Service to run script automatically  | Low    | Medium | ``systemd`` service / cron so the notifier runs automatically in the background

---

## 🔑 Key Decisions
Requirements that were discovered while building the project.
- **Security:** Use Telegram chat instead of email sent from my private account → avoid risking personal accounts  
- **Notifications:** Prefer Telegram private channel instead of chats → more reliable notifications on mobile
- **Connectivity:** You must have a stable internet connection → tether to a second phone with hotspot if unstable  
- **Improvement:** Status tracker in `main.py` → prevent spamming, avoid duplicate alerts 

---

## ⚡ Quick Ideas
- [ ] Notifier for **Filmpodium** → movie program updates  
- [ ] Notifier for **Berlin Marathon 2026** → registration alerts  
- [ ] Notifier for **Birthday Database** → reminders  

---

## 📆 Review Notes
- Last reviewed: **2025-09-22**  
- Next review: **TBD**

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

