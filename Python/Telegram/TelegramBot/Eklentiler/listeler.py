#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters

@Client.on_message(Filters.command(['admin'],['!','.','/']))
def admin(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Yönetici Listesini Çıkartıyorum..")
    else:
        kekik = message.reply("Yönetici Listesini Çıkartıyorum..", reply_to_message_id=cevaplanan_mesaj.message_id)
    
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
                    
        kekik.edit(f'**Yönetici Listesi**:\n{kurucu}{adminler}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.command(['bot'],['!','.','/']))
def bot(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Bot Listesini Çıkartıyorum..")
    else:
        kekik = message.reply("Bot Listesini Çıkartıyorum..", reply_to_message_id=cevaplanan_mesaj.message_id)

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":
        botlar = ""

        for bot in client.get_chat_members(message.chat.id, filter="bots"):
            botlar += f" 🤖 -> @{bot.user.username}\n"

        kekik.edit(f'**Bot Listesi**:\n{botlar}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.command(['silik'],['!','.','/']))
def silik(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Silinmiş Hesapları Sayıyorum..")
    else:
        kekik = message.reply("Silinmiş Hesapları Sayıyorum..", reply_to_message_id=cevaplanan_mesaj.message_id)

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in client.iter_chat_members(message.chat.id):
            if kisi.user.is_deleted:
                sayac += 1

        kekik.edit(f'__Silik Üye Sayısı__ : `{sayac}`', disable_web_page_preview=True)


@Client.on_message(Filters.command(['hayalet'],['!','.','/']))
def hayalet(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Hayalet Hesapları Sayıyorum..")
    else:
        kekik = message.reply("Hayalet Hesapları Sayıyorum..", reply_to_message_id=cevaplanan_mesaj.message_id)

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in client.iter_chat_members(message.chat.id):
            if kisi.user.status in ("long_time_ago", "within_month"):
                sayac += 1

        kekik.edit(f'__Hayalet üye sayısı__ : `{sayac}`', disable_web_page_preview=True)