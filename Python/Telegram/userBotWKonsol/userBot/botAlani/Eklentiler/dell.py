# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Message, Client, Filters
import asyncio

async def admin_kontrol(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    durum_kontrol = await client.get_chat_member(
        chat_id =   chat_id,
        user_id =   user_id
    )
    yonetici = [
        "creator",
        "administrator"
    ]

    if durum_kontrol.status not in yonetici:
        return False
    else:
        return True

@Client.on_message(Filters.command("dell", ['!','.','/']))
async def purge(client, message):
    # < Başlangıç
    uyku = await message.edit("__asyncio.sleep(0.3)__")
    await asyncio.sleep(0.3)
    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await uyku.delete()
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__içinden geçmek istediğiniz yerden mesaj yanıtlayın__")
        return
    
    if message.chat.type in ("supergroup", "channel"):
        if await admin_kontrol(message):
            await ilk_mesaj.edit(f"Admin değilmişim :)\n\n`{message.from_user.id}` __!=__ `{bilgiler['kurucu']}`")
            await asyncio.sleep(2)
            await ilk_mesaj.delete()
            return
    
    elif message.chat.type in ["private", "bot", "group"]:
        await ilk_mesaj.edit("`Bu komutu burda kullanamazsın..`")
        await asyncio.sleep(2)
        await ilk_mesaj.delete()
        return
    
    silinecek_mesaj_idleri = []
    silinen_mesaj_sayisi = 0

    if message.reply_to_message:
        for say_mesaj_id in range(message.reply_to_message.message_id, message.message_id):
            silinecek_mesaj_idleri.append(say_mesaj_id)

            if len(silinecek_mesaj_idleri) == 100: #TG_MAX_SELECT_LEN
                await client.delete_messages(
                    chat_id     = message.chat.id,
                    message_ids = silinecek_mesaj_idleri,
                    revoke      = True
                    )
                silinen_mesaj_sayisi += len(silinecek_mesaj_idleri)
                silinecek_mesaj_idleri = []

        if len(silinecek_mesaj_idleri) > 0:
            await client.delete_messages(
                chat_id     = message.chat.id,
                message_ids = silinecek_mesaj_idleri,
                revoke      = True
                )
            silinen_mesaj_sayisi += len(silinecek_mesaj_idleri)

    await ilk_mesaj.edit(f"`<u>{silinen_mesaj_sayisi}</u> Adet Mesaj Silindi`")
    await asyncio.sleep(3)
