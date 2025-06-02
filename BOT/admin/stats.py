import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


async def getallgc():
    from mongodb import gcdb
    return gcdb.find({}, {"_id": 0})


@Client.on_message(filters.command("stats", [".", "/"]))
async def stats(Client, message):
    try:
        user_id = str(message.from_user.id)
        
        # Load OWNER_ID from JSON
        with open("FILES/config.json", "r", encoding="utf-8") as config_file:
            OWNER_ID = json.load(config_file).get("OWNER_ID", [])

        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @lord_hanumant_bot !</b>"""
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        # Fetch and process data
        get_all_chats = list(await getallchat())  # Ensure these are iterable lists
        get_all_gc = list(await getallgc())
        get_all_user = list(await getallusers())

        # Count chats and gift codes
        chats = len(get_all_chats)
        total_gc = len(get_all_gc)
        total_user = len(get_all_user)

        # Process gift codes
        redeemed = sum(1 for item in get_all_gc if item.get("status") == "USED")

        # Process user statistics
        free_user = sum(1 for item in get_all_user if item.get("status") == "FREE")
        premium_user = sum(1 for item in get_all_user if item.get("status") == "PREMIUM")
        paid_user = sum(1 for item in get_all_user if "N/A" not in item.get("plan", "N/A"))

        active_ratio = premium_user * 3

        # Format response message
        done = f"""<b>
HANUMAN Checker ⚡ @lord_hanumant_bot Statistics ✅
━━━━━━━━━━━━━━ 
Total Commands : 52
Database Type : MongoDB
Total Registered Users : {total_user}
Total Free Users : {free_user}
Total Premium Users : {premium_user}
Total Authorized Chats : {chats}
Total Giftcode Generated : {total_gc}
Total Giftcode Redeemed : {redeemed}
Total Active Users Ratio : {active_ratio}

Status : Running
Checked On : {message.date}
    </b> """

        await message.reply_text(done, reply_to_message_id=message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"An error occurred: {e}", reply_to_message_id=message.id)
