# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import time
import requests

@Client.on_message(Filters.command(['gg'], ['!','.', '/']))                 # .gg Komutu Kullanıldığı Zaman
async def googleNasilKullanilir(client, message):                                 # fonksiyon oluşturuyoruz
    await message.edit("Bekleyin..")

    girilen_yazi = message.text                                             # komut ile birlikle mesajı tut
    if len(girilen_yazi.split()) == 1:                                      # eğer sadece komut varsa, girdi yoksa
        await message.edit("Arama yapabilmek için kelime girmelisiniz..")           # uyarı ver
        return                                                              # geri dön

    await message.edit("Aranıyor...")                                               # Mesajı Düzenle
    basla = time()                                                          # Zamanı Başlat
    girdi = " ".join(girilen_yazi.split()[1:])                              # girdiyi komuttan ayrıştır

    mesaj = f"Aranan Kelime : `{girdi}`\n\n"                                # Mesaj'ı Başlatıyoruz

    ara = girdi.replace(" ", "+")                                           # boşlukları + ya çeviriyoruz
    numune = f"https://da.gd/s?url=https://lmgtfy.com/?q={ara}%26iie=1"     # nasilgooglekullanilir linkimize ekliyoruz
    api_tepki = requests.get(numune).text                                   # api tepkisini alıyoruz

    if api_tepki:                                                           # eğer tepki varsa
        mesaj += f"🔍 [{girdi}]({api_tepki.rstrip()})"                      # Mesaja Ekle
        bitir = time()                                                      # Zamanı Durdur
        sure = bitir - basla                                                # Duran - Başlayan Zaman
        mesaj += f"\n\nTepki Süresi : `{str(sure)[:4]} sn`"                 # Mesaja Ekle
        try:                                                                # Dene
            await message.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
        except Exception as hata_mesaji:                                    # Başaramazsan
            await message.edit(hata_mesaji)                                         # Hatayı Söyle
    else:                                                                   # Eğer tepki yoksa
        await message.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..")      # uyarı ver