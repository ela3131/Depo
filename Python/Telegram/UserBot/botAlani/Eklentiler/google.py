# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import time
from google_search_client.search_client import GoogleSearchClient
import ast

@Client.on_message(Filters.command(['google'], ['!','.','/']))
async def google(client, message):
    await message.edit("Bekleyin..")
    
    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await message.edit("Arama yapabilmek için kelime girmelisiniz..")
        return
    await message.edit("Aranıyor...")
    
    basla = time()
    girdi = " ".join(girilen_yazi.split()[1:])
    mesaj = f"Aranan Kelime : `{girdi}`\n\n"
    
    istek = GoogleSearchClient()
    sonuclar = istek.search(girdi).to_json()
    
    if sonuclar:
        i = 1
        for sonuc in ast.literal_eval(sonuclar):
            mesaj += f"🔍 [{sonuc['title']}]({sonuc['url']})\n"
            i += 1
            if i == 5:
                break
        
        bitir = time()
        sure = bitir - basla
        mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"
        
        try:
            await message.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
        except Exception as hata:
            await message.edit(hata)
    else:
        await message.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..")