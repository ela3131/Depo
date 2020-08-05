# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, Filters
import pyfiglet
import asyncio

@Client.on_message(Filters.command(['figlet'], ['!','.','/']) & Filters.me)
async def figlet(client, message):
    await asyncio.sleep(0.3)
    await message.edit("‌‌‎__asyncio.sleep(0.3)__")

    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await message.edit("__bişiler söyle__")                 # uyarı ver
        return                                                  # geri dön

    neDedi = " ".join(girilen_yazi.split()[1:])                 # sözü komuttan ayır

    sonuc = pyfiglet.figlet_format(neDedi)
    await asyncio.sleep(0.3)
    await message.edit(f"‌‌‎`{sonuc}`")
