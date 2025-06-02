import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import error_log


@Client.on_message(filters.command("cs", [".", "/"]))
async def cmd_cs(Client, message):
    try:
        sender_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if sender_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @lord_hanumant_bot !</b>"""
            await message.reply_text(resp, message.id)
            return

        # Validate command format
        command_parts = message.text.split(" ")
        if len(command_parts) != 4:
            resp = """<b>Invalid Format ⚠️

Usage: /cs <user_id> <module> <value>
Example: /cs 123456789 credits 100</b>"""
            await message.reply_text(resp, message.id)
            return

        _, user_id, module, value = command_parts
        
        # Check if user exists
        user_exists = await getuserinfo(user_id)
        if not user_exists:
            resp = f"""<b>User Not Found ⚠️

User ID: {user_id}
Message: This user is not registered in the database.
Please ask the user to /register first.</b>"""
            await message.reply_text(resp, message.id)
            return
        
        # Normalize module name to lowercase
        module = module.lower()
        
        # Valid modules list
        valid_modules = ["credit", "totalkey", "plan", "status", "expiry"]
        if module not in valid_modules:
            resp = f"""<b>Invalid Module ⚠️

Valid modules: {', '.join(valid_modules)}
Example: /cs 123456789 plan Lifetime</b>"""
            await message.reply_text(resp, message.id)
            return
        
        # Convert value to appropriate type based on module
        if module in ["credit", "totalkey"]:
            try:
                value = int(value)
            except ValueError:
                resp = """<b>Invalid value ⚠️

For credit and totalkey, please provide a numeric value.
Example: /cs 123456789 credit 100</b>"""
                await message.reply_text(resp, message.id)
                return
        
        # Apply the update
        await updateuserinfo(user_id, module, value)
        
        # Verify the update was successful
        updated_user = await getuserinfo(user_id)
        if updated_user and str(updated_user.get(module)) == str(value):
            update_status = "✅ Successful"
        else:
            update_status = "❌ Failed"

        resp = f"""<b>
Custom Info Update
━━━━━━━━━━━━━━
User_ID : {user_id}
Key_Name : {module}
Key_Value : {value}
Status: {update_status}

Current User Data:
• Credit: {updated_user.get('credit', 'N/A')}
• Plan: {updated_user.get('plan', 'N/A')}
• Status: {updated_user.get('status', 'N/A')}
• Expiry: {updated_user.get('expiry', 'N/A')}
</b> """
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())