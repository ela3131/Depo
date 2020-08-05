# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, Filters
import io, os, sys, traceback
import time, asyncio, requests

@Client.on_message(Filters.command(["eval", "py"], ['!','.','/']) & Filters.me)
async def eval(client, message):
    status_message = await message.reply_text("`İşleniyor...`")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Başarılı"

    final_output = "<b>Kod</b>: <code>{}</code>\n\n<b>Çıktı</b>:\n<code>{}</code> \n".format(
        cmd,
        evaluation.strip()
    )

    if len(final_output) > 4096:
        with open("eval.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document="eval.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("eval.text")
        await status_message.delete()
    else:
        await status_message.edit(final_output)
    await message.delete()

async def aexec(code, client, message):
    exec(
        f'async def __aexec(client, message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)


@Client.on_message(Filters.command(["exec", "sh"], ['!','.','/']) & Filters.me)
async def execution(_, message):
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "__Hata Yok__"
    o = stdout.decode()
    if not o:
        o = "__Çıktı Yok__"

    OUTPUT = ""
    OUTPUT += f"<b>Sorgu:</b>\n<u>Komut:</u>\n<code>{cmd}</code>\n\n"
    OUTPUT += f"<u>PID</u>: <code>{process.pid}</code>\n\n"
    OUTPUT += f"<b>stderr</b>: \n<code>{e}</code>\n\n"
    OUTPUT += f"<b>stdout</b>: \n<code>{o}</code>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("exec.text")
    else:
        await message.reply_text(OUTPUT)
    await message.delete()

@Client.on_message(Filters.command(["ip"], ['!','.','/']) & Filters.me)
async def public_ip(client, message):
    ip = requests.get('https://api.ipify.org').text
    await message.reply_text(f'<b>Bot IP Address:</b>\n<code>{ip}</code>', parse_mode='html')