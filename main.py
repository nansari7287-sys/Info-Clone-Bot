import os
import asyncio
import logging
import json
import re
import time
from datetime import datetime
from threading import Thread

# ==========================================
# 🛑 CRITICAL RENDER FIX: EVENT LOOP SETUP
# WARNING: Ye Pyrogram import hone se PEHLE aana chahiye!
# ==========================================
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Ab hum safely Pyrogram aur baaki modules import kar sakte hain
from pyrogram import Client, filters, idle
from flask import Flask
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# ==========================================
# ⚙️ SYSTEM CONFIGURATIONS
# ==========================================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FrexxxyOSINT")

# 🔐 API & SESSION CREDENTIALS FETCHED FROM .env
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")

TARGET_BOT = os.getenv("TARGET_BOT", "@Randominsight_bot")
SYSTEM_NAME = os.getenv("SYSTEM_NAME", "@frexxxy")

# 👑 ADMIN & AUTHORIZATION
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
AUTHORIZED_USERS = [OWNER_ID, ADMIN_ID]
START_TIME = time.time()

# ==========================================
# 🌐 FLASK WEB SERVER (For Render 24/7 Uptime)
# ==========================================
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return f"🤖 {SYSTEM_NAME} VIP Engine is Running Seamlessly on Render!"

def run_server():
    # Flask thread ke liye alag event loop set karna zaroori hai
    asyncio.set_event_loop(asyncio.new_event_loop())
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)

# ==========================================
# 🤖 PYROGRAM SESSION INITIALIZATION
# ==========================================
app = Client(
    "vip_session_engine",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# ==========================================
# 🎨 VIP MENU GENERATOR
# ==========================================
def get_vip_menu(user):
    return (
        f"✦ ━━━━━━━━━━━━━━━━━━━━ ✦\n"
        f"👑 **𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐕𝐈𝐏 𝐏𝐀𝐍𝐄𝐋** 👑\n"
        f"✦ ━━━━━━━━━━━━━━━━━━━━ ✦\n"
        f"👤 **𝐔𝐬𝐞𝐫:** `{user.first_name}` | 🆔 `{user.id}`\n\n"
        f"🌐 **𝗜𝐍𝐅𝐎 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒**\n"
        f"• 📱 `/num` ➾ Phone Details\n"
        f"• 💳 `/aadhar` ➾ Aadhaar Details\n"
        f"• 👨‍👩‍👧 `/familyinfo` ➾ Family Details\n"
        f"• 🚙 `/vnum` ➾ Vehicle to Mobile\n"
        f"• 🇵🇰 `/paknum` ➾ Pak Database\n"
        f"• 📱 `/mpnum` ➾ MP State Num Details\n\n"
        f"🏦 **𝐅𝐈𝐍𝐀𝐍𝐂𝐄 & 𝐆𝐎𝐕𝐓**\n"
        f"• 💳 `/advpan` ➾ Advance PAN\n"
        f"• 🏦 `/ifsc` ➾ Bank IFSC\n"
        f"• 📄 `/gst` ➾ Business Data\n"
        f"• 📍 `/pincode` ➾ Area Pincode\n"
        f"• 🗳️ `/voter` ➾ Voter ID Details\n"
        f"• 📋 `/ration` ➾ Ration Card\n\n"
        f"🛢️ **𝐔𝐓𝐈𝐋𝐈𝐓𝐈𝐄𝐒 & 𝐒𝐎𝐂𝐈𝐀𝐋**\n"
        f"• 📞 `/tgnum` ➾ Telegram User Info\n"
        f"• 🛢️ `/lpg` ➾ LPG Consumer\n"
        f"• 🛢️ `/bharatgas` ➾ Bharat Gas\n"
        f"• ⛽ `/hpgas` ➾ HP Gas\n"
        f"• 👤 `/myid` ➾ Check your User ID\n\n"
        f"⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}\n"
        f"✦ ━━━━━━━━━━━━━━━━━━━━ ✦"
    )

# ==========================================
# ⏳ HACKER LOADING ANIMATION
# ==========================================
async def run_loading_animation(message):
    anim_msg = await message.reply_text("```ini\n▒▒▒▒▒▒▒▒▒▒ 0% [CONNECTING]\n```")
    bars = [
        "```ini\n███▒▒▒▒▒▒▒ 25% [CHECKING DB]\n```",
        "```ini\n██████▒▒▒▒ 50% [GETTING INFO]\n```",
        "```ini\n█████████▒ 80% [PROCESSING]\n```",
        "```ini\n██████████ 100% [COMPLETED]\n```"
    ]
    for bar in bars:
        await asyncio.sleep(0.6) 
        try:
            await anim_msg.edit_text(bar)
        except:
            pass
    return anim_msg

# ==========================================
# 🎮 BASIC COMMAND HANDLERS
# ==========================================
@app.on_message(filters.command("ping", prefixes=["/", ".", "!"]))
async def cmd_ping(client, message):
    if message.from_user.id not in AUTHORIZED_USERS: return
    uptime = str(datetime.timedelta(seconds=int(time.time() - START_TIME)))
    msg = await message.reply_text(f"⚡ **SYSTEM STATUS**\n━━━━━━━━━━━━\n🕒 Uptime: `{uptime}`\n✅ Status: `Online & Active`\n🛡️ Protection: `Enabled`")
    await asyncio.sleep(15)
    await msg.delete()

@app.on_message(filters.command("myid", prefixes=["/", ".", "!"]))
async def cmd_myid(client, message):
    await message.reply_text(f"👤 **Aapki Telegram ID:** `{message.from_user.id}`\n\n⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}")

@app.on_message(filters.command("auth", prefixes=["/", ".", "!"]) & filters.private)
async def cmd_auth(client, message):
    if message.from_user.id not in [OWNER_ID, ADMIN_ID]:
        return await message.reply_text("🚫 **Access Denied.**")
    if len(message.command) < 2:
        return await message.reply_text("❌ **Format:** `/auth [User_ID]`")
    try:
        user_id = int(message.command[1])
        if user_id not in AUTHORIZED_USERS:
            AUTHORIZED_USERS.append(user_id)
            await message.reply_text(f"✅ User `{user_id}` ko VIP Database access mil gaya hai.")
        else:
            await message.reply_text("ℹ️ User pehle se VIP list me hai.")
    except ValueError:
        await message.reply_text("❌ **Invalid ID!**")

@app.on_message(filters.command(["start", "help", "menu"], prefixes=["/", ".", "!"]))
async def cmd_start(client, message):
    if message.chat.type.name == "PRIVATE" and message.from_user.id not in AUTHORIZED_USERS:
        return await message.reply_text(f"🛑 **ACCESS DENIED** 🛑\n\nIs Premium panel ko use karne ke liye Owner se permission lijiye.\n\n⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}")
    
    vip_menu = get_vip_menu(message.from_user)
    await message.reply_text(vip_menu, disable_web_page_preview=True)

# ==========================================
# 🚀 CORE OSINT ENGINE (TARGET BOT RELAY)
# ==========================================
@app.on_message(filters.command([
    "num", "aadhar", "familyinfo", "vnum", "paknum", "pincode", 
    "advpan", "tgnum", "ifsc", "gst", "lpg", "bharatgas", 
    "voter", "ration", "mpnum", "hpgas"
], prefixes=["/", ".", "!"]))
async def process_lookup(client, message):
    if message.chat.type.name == "PRIVATE" and message.from_user.id not in AUTHORIZED_USERS:
        return await message.reply_text(f"🛑 **ACCESS DENIED** 🛑\n\nAapke paas is command ka access nahi hai.\n⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}")

    if len(message.command) < 2:
        return await message.reply_text(f"❌ **Data missing!**\nSahi format: `/{message.command[0]} [value]`")

    try:
        try:
            sent_req = await client.send_message(TARGET_BOT, message.text)
        except Exception as e:
            return await message.reply_text(f"❌ **Database Connection Error:** Ensure you have started {TARGET_BOT}.\nError: {e}")

        anim_msg = await run_loading_animation(message)

        target_response = None
        for _ in range(25): 
            await asyncio.sleep(2)
            async for log in client.get_chat_history(TARGET_BOT, limit=5):
                if log.id > sent_req.id:
                    text_content = (log.text or log.caption or "").lower()
                    ignore_words = ["wait", "searching", "processing", "loading", "fetching", "scanning"]
                    
                    if any(word in text_content for word in ignore_words) and not log.document:
                        continue 
                    
                    target_response = log
                    break
            if target_response: 
                break

        if not target_response:
            return await anim_msg.edit_text("❌ **Timeout:** Database server is taking too long. Please try again.")

        raw_text = ""
        
        if target_response.document:
            await anim_msg.edit_text("```ini\n📂 [DOWNLOADING SECURE FILE]\n```")
            path = await client.download_media(target_response)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                raw_text = f.read()
            os.remove(path)
        else:
            raw_text = target_response.text or target_response.caption or ""

        if not raw_text or len(raw_text.strip()) < 2:
            return await anim_msg.edit_text("❌ **No Records Found in Database.**")

        clean_output = re.sub(r"⚡ Designed.*|@\w+|powered by.*", "", raw_text, flags=re.IGNORECASE).strip()

        command_used = message.command[0].upper()
        if "{" in clean_output or ":" in clean_output:
            final_msg = f"**🗂️ {command_used} INTELLIGENCE REPORT**\n```json\n{clean_output}\n```\n\n⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}"
        else:
            final_msg = f"**🗂️ {command_used} INTELLIGENCE REPORT**\n`{clean_output}`\n\n⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : {SYSTEM_NAME}"

        await anim_msg.delete()

        sent_message = None
        if len(final_msg) > 4000:
            for i in range(0, len(final_msg), 4000):
                sent_message = await message.reply_text(final_msg[i:i+4000])
                await asyncio.sleep(1)
        else:
            sent_message = await message.reply_text(final_msg)

        if sent_message:
            await asyncio.sleep(30)
            try:
                await sent_message.delete()
                await message.reply_text(f"🧹 **Data has been auto-deleted after 30 seconds for your privacy.**\n\n⚡ 𝐏𝐨𝐰𝐞𝐫 𝐁𝐲 : {SYSTEM_NAME}")
            except:
                pass

    except Exception as e:
        try:
            await message.reply_text(f"❌ **System Error:** Connection disrupted.")
        except:
            pass

# ==========================================
# 🔥 MAIN EXECUTION PROCESS
# ==========================================
if __name__ == "__main__":
    # 1. Start Web Server in a background thread for Render Port Binding
    Thread(target=run_server, daemon=True).start()
    
    # 2. Start Pyrogram Engine
    print("⏳ Initializing VIP Session Engine...")
    print(f"✅ Bridge Connected to {TARGET_BOT}")
    app.run()
