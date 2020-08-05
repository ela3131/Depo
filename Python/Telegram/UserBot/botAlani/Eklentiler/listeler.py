# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters

@Client.on_message(Filters.command(['admin'],['!','.','/']))
async def admin(client, message):
    await message.edit("Yönetici Listesini Çıkartıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":
        kurucu = ""
        adminler = ""
        
        for yonetici in client.get_chat_members(message.chat.id, filter="administrators"):
            if not yonetici.user.is_bot:
                if yonetici.status == "creator":
                    if yonetici.user.username: kurucu += f"👑 -> @{yonetici.user.username}\n\n"
                    else: kurucu += f"👑 -> [{yonetici.user.first_name}](tg://user?id={yonetici.user.id})\n\n"
                        
                if yonetici.status == "administrator":
                    if yonetici.user.username: adminler += f" ⛑ -> @{yonetici.user.username}\n"
                    else: adminler += f" ⛑ -> [{yonetici.user.first_name}](tg://user?id={yonetici.user.id})\n"
                    
        await message.edit(f'**Yönetici Listesi**:\n{kurucu}{adminler}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.command(['bot'],['!','.','/']))
async def bot(client, message):
    await message.edit("Bot Listesini Çıkartıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":
        botlar = ""

        for bot in client.get_chat_members(message.chat.id, filter="bots"):
            botlar += f" 🤖 -> @{bot.user.username}\n"

        await message.edit(f'**Bot Listesi**:\n{botlar}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.command(['silik'],['!','.','/']))
async def silik(client, message):
    await message.edit("Silinmiş Hesapları Sayıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in client.iter_chat_members(message.chat.id):
            if kisi.user.is_deleted:
                sayac += 1

        await message.edit(f'__Silik Üye Sayısı__ : `{sayac}`', disable_web_page_preview=True)


@Client.on_message(Filters.command(['hayalet'],['!','.','/']))
async def hayalet(client, message):
    await message.edit("Hayalet Hesapları Sayıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in client.iter_chat_members(message.chat.id):
            if kisi.user.status in ("long_time_ago", "within_month"):
                sayac += 1

        await message.edit(f'__Hayalet üye sayısı__ : `{sayac}`', disable_web_page_preview=True)