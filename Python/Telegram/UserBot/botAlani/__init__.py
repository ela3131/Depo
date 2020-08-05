# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
import json

bilgiler = json.load(open("bilgiler.json"))

betikUserBot        = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = "@betikUserBot",                      # Fark Etmez
    plugins         = dict(root="botAlani/Eklentiler")
)

from time import time, sleep
from os import listdir

@betikUserBot.on_message(Filters.me & Filters.command(['yardim'], ['!','.','/']))
async def yardim_mesaji(client, message):
    await message.edit("Bekleyin..")
    basla = time()
    await message.edit("Aranıyor...")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
    Ben @BetikSonu'nda yaratıldım.\n
    Kaynak kodlarım [Burada](https://github.com/BetikSonu/)
    Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += "__Eklentilerim;__\n"
    for dosya in listdir("./botAlani/Eklentiler/"):
        if not dosya.endswith(".py"): continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{str(sure)[:4]} sn`"

    try: await message.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji: await message.edit(hata_mesaji)

@betikUserBot.on_message(Filters.me & Filters.command(['eklenti'], ['!','.','/']))
async def eklenti_gonder(client, message):
    await message.edit("__Bekleyin..__")
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await message.edit("`DosyaAdı` **Girmelisin!**")        # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in listdir("botAlani/Eklentiler"):
        await message.delete()
        await message.reply_document(f"./botAlani/Eklentiler/{dosya}.py")
    else : await message.edit('**Dosya Bulunamadı!**')