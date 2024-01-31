#!/usr/bin/env python
#
# Python code which automatically posts Message in a Telegram Group if any new update is found.
# Intended to be run on every push
# USAGE : python3 post.py
# See README for more.
#
# Copyright (C) 2022 PrajjuS <theprajjus@gmail.com>
#
# Credits: Ashwin DS <astroashwin@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import re
import telebot
import os
import json
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
from NoobStuffs.libtelegraph import TelegraphHelper

BOT_TOKEN = "6605832961:AAG5_95xJDl20-YW4jjgauu1gP2p7E1fCUo"
CHAT_ID = "-1002018496570"

# Init bot
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="MarkdownV2")

# Init telegraph
telegraph = TelegraphHelper("Notification", "https://t.me/SakuraKernelNoticeBot")

# Send Message
def tg_message():
    msg = os.popen('cat out')
    bot.send_message(CHAT_ID, msg.read())

# Final stuffs
tg_message()
print("Successfull")
