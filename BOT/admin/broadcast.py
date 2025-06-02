import asyncio
import json
import threading
import time
from datetime import timedelta
from pyrogram import Client, filters
from FUNC.defs import *
from FUNC.usersdb_func import *


# Forward Message to a User or Chat
async def message_forward_xcc(original_message, user_id):
    try:
        await original_message.copy(chat_id=user_id)
        return True
    except Exception:
        return False


# Start Broadcast Thread
@Client.on_message(filters.command("brod", [".", "/"]))
def multi(client, message):
    t1 = threading.Thread(target=bcall, args=(client, message))
    t1.start()


# Thread Target Function
def bcall(client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(brod_cmd(client, message))
    loop.close()


# Broadcast Command Logic
async def brod_cmd(client, message):
    try:
        user_id = str(message.from_user.id)
        with open("FILES/config.json", "r", encoding="utf-8") as config_file:
            OWNER_ID = json.load(config_file)["OWNER_ID"]

        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner - <a href="https://t.me/lord_hanumant_bot">Hanuman</a> !</b>"""
            await message.reply_text(resp, message.id)
            return

        original_message = message.reply_to_message
        if not original_message:
            await message.reply_text("<b>Please reply to a message to broadcast.</b>")
            return

        all_user = []
        get_user = await getallusers()
        get_chat = await getallchat()

        # Use set to avoid duplicates completely
        all_user_set = set()
        
        # Add users
        for user in get_user:
            all_user_set.add(int(user["id"]))
        
        # Add chats
        for chat in get_chat:
            all_user_set.add(chat["id"])
        
        # Convert back to list
        all_user = list(all_user_set)

        text = f"""<b>
Broadcast Started ✅
━━━━━━━━━━━━━━
Total Audience: {len(all_user)}

Status: In Progress...</b>"""
        await message.reply_text(text, message.id)

        sent_brod = 0
        not_sent = 0
        start = time.perf_counter()
        worker_num = 25

        # Broadcasting in batches
        for i in range(0, len(all_user), worker_num):
            batch = all_user[i:i + worker_num]
            results = await asyncio.gather(
                *[message_forward_xcc(original_message, user) for user in batch],
                return_exceptions=True
            )
            for result in results:
                if result is True:
                    sent_brod += 1
                else:
                    not_sent += 1

        # Calculate Time Taken
        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)

        done = f"""<b>
Broadcast Completed Successfully ✅
━━━━━━━━━━━━━━
Total Audience: {len(all_user)}
Message Sent: {sent_brod}
Failed to Send: {not_sent}
Success Ratio: {int(sent_brod * 100 / len(all_user))}%

Time Taken: {hour} Hour(s) {min} Minute(s)
        </b>"""

        await message.reply_text(done, message.id)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())