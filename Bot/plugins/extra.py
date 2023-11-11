import os, random, time, sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot import TRIGGERS as trg, OWNER_ID

@Client.on_message(filters.user(OWNER_ID) & filters.command('restart', prefixes=trg))
async def restart_bot(client: Client, message: Message):  
    msg = await message.reply("Restarting...")
    time.sleep(5) # Adding a 5-second delay before restarting
    os.execl(sys.executable, sys.executable, "-m", "Bot")

@Client.on_ready()
async def bot_restarted(client: Client):
    me = await client.get_me()
    restart_notif = f"Bot is successfully restarted! @{me.username}"
    msg = await message.reply(restart_notif, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Dev', url='https://t.me/BashAFK')]]))
