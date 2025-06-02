import json
from pyrogram import Client, filters
from FUNC.defs import error_log

@Client.on_message(filters.command("addproxy", [".", "/"]))
async def add_proxy(client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @lord_hanumant_bot !</b>"""
            await message.reply_text(resp)
            return

        # Get proxy from message
        try:
            proxy = message.text.split(" ", 1)[1].strip()
        except IndexError:
            resp = """<b>Invalid Format ⚠️

Please provide proxy in format:
/addproxy IP:PORT:USERNAME:PASSWORD

Example:
/addproxy 38.153.152.244:9594:jklmthvu:zcr0x1b0we2m</b>"""
            await message.reply_text(resp)
            return

        # Validate proxy format
        try:
            ip, port, username, password = proxy.split(":")
            # Basic validation
            if not all([ip, port, username, password]):
                raise ValueError
        except ValueError:
            resp = """<b>Invalid Proxy Format ⚠️

Please provide proxy in format:
IP:PORT:USERNAME:PASSWORD

Example:
38.153.152.244:9594:jklmthvu:zcr0x1b0we2m</b>"""
            await message.reply_text(resp)
            return

        # Add proxy to file
        with open("FILES/proxy.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{proxy}")

        resp = f"""<b>
Proxy Added Successfully ✅

Proxy: <code>{proxy}</code>

Message: Proxy has been added to the proxy list.</b>"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"An error occurred: {str(e)}") 