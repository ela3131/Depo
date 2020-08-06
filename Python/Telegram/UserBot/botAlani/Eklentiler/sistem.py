# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import requests, os, platform

@Client.on_message(Filters.command(['sistem'], ['!','.','/']) & Filters.me)
async def sistem(client, message):
    await asyncio.sleep(0.3)
    await message.edit("__asyncio.sleep(0.3)__")
    
    try:
        mesaj = f"""__Kullanıcı :__ `{os.getlogin()}@{platform.node()}`
    __IP :__ `{requests.get('http://ip.42.pl/raw').text}`
    __OS :__ `{platform.system()} | {platform.release()}`
    __İşlemci :__ `{platform.processor()}`"""
        await message.edit(mesaj)
    
    except Exception as hata: await message.edit(f"__başaramadık abi__\n\n\t`{hata}`")
