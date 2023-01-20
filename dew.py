# DewChatGPT, telegram text based bot with Artificial Intelligence
# Copyright (C) 2023  Leoksu

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from stuff.string import START_TEXT, HELP_TEXT, ABOUT_TEXT, MENU_TEXT
from pyrogram.errors import MessageNotModified
from pyrogram import idle, Client, filters
from stuff.configs import *
from asyncio import sleep
import requests
import random
import glob
import sys
import os
import re

logger = getLogger("DewLogs")

dewlog = f"dews{sys.argv[6]}.log" if len(sys.argv) > 6 else "dews.log"
if os.path.exists(dewlog):
    os.remove(dewlog)

_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
)

logger.info("[---------->>> Starting your deployement <<<----------]")
logger.info("Initializing...")

ghoul = Client(
            ".dew",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )

bot_id = int(BOT_TOKEN.split(":")[0])

logger.info("Loading modules...")

def generate_text(prompt):
    data = {
        'prompt': prompt,
        'model': 'text-ada-001',
        'temperature': 0.5,
        'max_tokens': 1024,
        'n': 1,
        'stop': None,
        'temperature': 0.9,
        'top_p': 0.3,
        'frequency_penalty': 0.5,
    }
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
    response = requests.post('https://api.openai.com/v1/completions', json=data, headers=headers)
    return response.json()

@ghoul.on_message(filters.private & ~filters.edited & ~filters.regex(r'^/'))
async def dewgpt(client, message):
    dewword = {
        1: "I'm sorry, as poor robots, for now I can only understand word. tell @aethersghoul don't be lazy, update me >:(",
        2: "Like i told you before, I only understand word",
        3: "Please use normal word :)",
    }
    counter = 1
    if not message.text:
        await message.reply_text(dewword[counter])
        counter += 1
        if counter > len(dewword):
            counter = 1
    else:
        chat_id = message.chat.id
        prompt = message.text
        await message._client.send_chat_action(chat_id, "typing")
        await sleep(3)
        response = generate_text(prompt)
        r_text = response["choices"][0]["text"]
        await message.reply(r_text)
        await message._client.send_chat_action(chat_id, "cancel")

logger.info("Successfully loaded GPT modules")

@ghoul.on_message(
    ~filters.private
    & filters.text
    & ~filters.regex(r'^/')
    & ~filters.edited,
    group=666,
)
async def chat(_, message):
    chat_id = message.chat.id
    dewresponses = [
        "Hello! How can I help you today?",
        "Hello! With Dewdrop here. I'm at your service",
        "Hey! I'm here ready to help you. What can I do for you?",
        "^&;/√%+[\(-$... Ahh Forget it, There's something for me to do? ",
    ]
    dewcall = random.choice(dewresponses)
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}dew[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        match2 = re.search(
            "[.|\n]{0,}dewdrop[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match and not match2:
            return
    await ghoul.send_chat_action(chat_id, "typing")
    await sleep(1)
    await message.reply_text(dewcall)
    await ghoul.send_chat_action(chat_id, "cancel")

logger.info("Successfully loaded DewCall modules")

@ghoul.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❔ HOW TO USE ME ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("📢 CHANNEL", url=f"https://t.me/TheGhostOrg"),
                InlineKeyboardButton("SOURCE 📦", url=f"https://github.com/Leoksu/DewChatGPT"),
            ],
            [
                InlineKeyboardButton("🤖 ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE 🔒", callback_data="close"),
            ],
            [
                InlineKeyboardButton("➕ ADD ME TO YOUR GROUP ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
   start_markup = InlineKeyboardMarkup(buttons)
   mention = message.from_user.mention
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT.format(mention),
          reply_markup=start_markup
       )
   else:
      pm_but = [InlineKeyboardButton("PM Dew's", url=f"https://t.me/{USERNAME}?start")]
      pm_msg = f"Hello {mention}! PM me if you have any questions on how to use me!"
      pm_markup = InlineKeyboardMarkup(pm_but)
      await message.reply_text(
          pm_msg,
          reply_markup=pm_markup
      )

@ghoul.on_message(filters.command(["help", f"help@{USERNAME}"]))
async def help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔙 BACK", callback_data="menu"),
            InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if message.chat.type == 'private':
        await message.reply_text(
            HELP_TEXT,
            reply_markup=reply_markup
        )
    else:
        pm_but = [InlineKeyboardButton("PM Dew's", url=f"https://t.me/{USERNAME}?start")]
        pm_msg = f"Hello! PM me if you have any questions on how to use me!"
        pm_markup = InlineKeyboardMarkup(pm_but)
        await message.reply_text(
            pm_msg,
            reply_markup=pm_markup
        )

logger.info("Successfully loaded help modules")

@ghoul.on_callback_query()
async def cb_handler(client: ghoul, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🔙 BACK", callback_data="menu"),
                InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("🔙 BACK", callback_data="menu"),
                InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )
        except MessageNotModified:
            pass

    elif query.data=="menu":
        buttons = [
            [
                InlineKeyboardButton("❔ HOW TO USE ME ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("📢 CHANNEL", url=f"https://t.me/TheGhostOrg"),
                InlineKeyboardButton("SOURCE 📦", url=f"https://github.com/Leoksu/DewChatGPT"),
            ],
            [
                InlineKeyboardButton("🤖 ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE 🔒", callback_data="close"),
            ],
            [
               InlineKeyboardButton("➕ ADD ME TO YOUR GROUP ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                MENU_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

logger.info("Successfully loaded start modules")


### https://github.com/dashezup/tgbot/blob/dev/plugins/ping.py ###
import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters

PING_DELAY_DELETE = 8
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


# https://gist.github.com/borgstrom/936ca741e885a1438c374824efb038b3
def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


main_filter = (
    filters.text
    & filters.incoming
    & ~filters.edited
)


@ghoul.on_message(main_filter & filters.regex("^/ping$"))
async def ping_pong(_, message: Message):
    """reply ping with pong and delete both messages"""
    start = time()
    reply = await message.reply_text("...", quote=True)
    delta_ping = time() - start
    await reply.edit_text(f"**Pong!**\n`{delta_ping * 1000:.3f} ms`")


@ghoul.on_message(main_filter & filters.regex("^/uptime$"))
async def get_uptime(_, message: Message):
    """/uptime Reply with readable uptime and ISO 8601 start time"""
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = _human_time_duration(int(uptime_sec))
    await message.reply_text(f"**Uptime**: `{uptime}`\n"
                             f"**Start time**: `{START_TIME_ISO}`",
                             quote=True)

logger.info("Successfully loaded ping modules")

logger.info("Successfully loaded all modules, Starting...")

async def main():
    await ghoul.start()
    logger.info(
        """
               --------------------------------------------------------------------------------------
                              Dew's has been started, see @TheGhostOrg for updates
               --------------------------------------------------------------------------------------
    """
    )
    await idle()

loop = asyncio.get_event_loop()

loop.run_until_complete(main())
logger.info(" --- Dew's has been stopped ---")
