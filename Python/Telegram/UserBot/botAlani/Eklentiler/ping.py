# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import datetime

@Client.on_message(Filters.command(['ping'], ['!','.','/']) & Filters.me)
async def ping(client, message):
    basla = datetime.datetime.now()
    await message.edit("Bekleyin..")

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds/10000
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await message.edit(mesaj)
    
    await asyncio.sleep(3)
    await message.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)
    await message.edit(mesaj)