# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import requests, os, platform

@Client.on_message(Filters.command(['sistem'], ['!','.','/']) & Filters.me)
async def sistem(client, message):
    await asyncio.sleep(0.3)
    await message.edit("‌‌‎__asyncio.sleep(0.3)__")

    mesaj = f"""Kullanıcı : {os.getlogin()}@{platform.node()}
IP : {requests.get('http://ip.42.pl/raw').text}
OS : {platform.system()} | {platform.release()}
İşlemci : {platform.processor()}"""

    await message.edit(mesaj)
