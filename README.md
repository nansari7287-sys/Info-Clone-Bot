<div align="center">
  <img src="https://i.ibb.co/gZhFNqLP/x.jpg" alt="Bot Logo" width="150">
  <h1>Telegram Proxy & Data Routing Bot</h1>
  <p>
    <b>A Pyrogram-based intermediary bot for automated querying, response parsing, and access control.</b>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/Framework-Pyrogram-blueviolet.svg" alt="Pyrogram">
    <img src="https://img.shields.io/badge/Web-Flask-lightgrey.svg" alt="Flask">
  </p>
</div>

---

## ⚙️ Core Logic & Architecture
This script acts as a seamless and secure middleman between authorized users and a hidden backend target bot. By utilizing a **Telegram User Session**, it automates data retrieval, scrubs sensitive watermarks, and delivers clean results without exposing the underlying target bot to end-users.

**Execution Flow:**
1. **Command Interception:** The bot listens for specific trigger commands (e.g., `/num`, `/aadhar`, `/vnum`, etc.).
2. **Access Verification:** Checks if the sender's Telegram `user_id` exists in the `AUTHORIZED_USERS` memory list.
3. **Query Routing:** Forwards the raw query payload to the predefined hidden `TARGET_BOT`.
4. **Async Polling:** Polls the target bot's chat history every 2 seconds, explicitly ignoring transitional states like "waiting", "loading", or "processing".
5. **Data Extraction & Scrubbing:**
   - If the response is a document, it downloads, reads the UTF-8 text, and deletes the local file.
   - Applies Regex (`re.sub`) to strip external branding, developer tags, and `@usernames` from the raw text.
6. **Delivery & Auto-Deletion:** Formats the output (JSON block or Markdown), chunks messages if they exceed Telegram's 4000-character limit, and schedules an automatic `message.delete()` after 30 seconds to clear chat history for privacy.

## 🛠 Technical Features
- **Strict Authorization System:** Only hardcoded `OWNER_ID` and `ADMIN_ID` can execute the `/auth` command to append new users to the active runtime list.
- **Smart Response Parser:** Handles both standard text replies and `.txt` document uploads from the target bot.
- **Pagination (Message Splitting):** Automatically chunks large payloads into sequential messages to prevent API `MessageTooLong` exceptions.
- **Event Loop Management:** Explicitly creates and sets a new asyncio event loop to prevent runtime errors in newer Python environments (3.10+) or cloud containers.
- **Daemon Web Server:** Runs a parallel Flask thread on `0.0.0.0` to bind to cloud provider ports, preventing container suspension and ensuring 24/7 uptime.

## 🚀 Setup & Deployment

### 1. Requirements & Dependencies
Make sure you have Python installed. Install the required libraries using:
```bash
pip install -r requirements.txt
