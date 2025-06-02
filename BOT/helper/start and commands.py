import asyncio
import time
from datetime import date
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FUNC.defs import *
from FUNC.usersdb_func import *


@Client.on_message(filters.command("cmds", [".", "/"]))
async def cmd_scr(client, message):
    try:
        WELCOME_TEXT = f"""
<b>Hello <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !

Hanuman  Checker  Has plenty of Commands . We Have Auth Gates , Charge Gates , Tools And Other Things .

Click Each of Them Below to Know Them Better .</b>
        """
        WELCOME_BUTTONS = [
            [
                InlineKeyboardButton("AUTH/B3/VBV", callback_data="AUTH"),
                InlineKeyboardButton("CHARGE", callback_data="CHARGE")
            ],
            [
                InlineKeyboardButton("TOOLS", callback_data="TOOLS"),
                InlineKeyboardButton("HELPER", callback_data="HELPER")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await message.reply(
            text=WELCOME_TEXT,
            reply_markup=InlineKeyboardMarkup(WELCOME_BUTTONS))

    except Exception:
        import traceback
        await error_log(traceback.format_exc())


async def callback_command(client, callback_query):
    try:
        WELCOME_TEXT = f"""
<b>Hello User !

Hanuman  Checker  Has plenty of Commands . We Have Auth Gates , Charge Gates , Tools And Other Things .

Click Each of Them Below to Know Them Better .</b>
        """
        WELCOME_BUTTONS = [
            [
                InlineKeyboardButton("AUTH/B3/VBV", callback_data="AUTH"),
                InlineKeyboardButton("CHARGE", callback_data="CHARGE")
            ],
            [
                InlineKeyboardButton("TOOLS", callback_data="TOOLS"),
                InlineKeyboardButton("HELPER", callback_data="HELPER")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await callback_query.edit_message_text(
            text=WELCOME_TEXT,
            reply_markup=InlineKeyboardMarkup(WELCOME_BUTTONS))

    except Exception:
        import traceback
        await error_log(traceback.format_exc())


@Client.on_message(filters.command("start", [".", "/"]))
async def cmd_start(Client, message):
    try:
        text = """<b>
Hanuman  Checker  ■□□
      </b>"""
        edit = await message.reply_text(text, message.id)
        await asyncio.sleep(0.5)

        text = """<b>
Hanuman  Checker  ■■■
     </b> """
        edit = await Client.edit_message_text(message.chat.id, edit.id, text)
        await asyncio.sleep(0.5)

        # Delete the loading message first
        await Client.delete_messages(message.chat.id, edit.id)

        text = f"""
<b>🌟 Hello <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!</b>

<b>Welcome aboard the Hanuman  Checker! 🚀</b>

<b>I am your go-to bot, packed with a variety of gates, tools, and commands to enhance your experience. Excited to see what I can do?</b>

<b>👇 Tap the <i>Register</i> button to begin your journey.</b>
<b>👇 Discover my full capabilities by tapping the <i>Commands</i> button.</b>

"""
        WELCOME_BUTTON = [
            [
                InlineKeyboardButton("Register", callback_data="register"),
                InlineKeyboardButton("Commands", callback_data="cmds")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        try:
            await Client.send_video(
                chat_id=message.chat.id,
                video = "https://t.me/YouBeingNaruto/5",  # Replace with your video URL or file_id
                caption=text,
                reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON)
            )
        except Exception as video_error:
            print(f"Video sending failed: {video_error}")
            # Fallback to text message if video fails
            await message.reply_text(
                text=text,
                reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON)
            )
    except:
        import traceback
        await error_log(traceback.format_exc())


async def register_user(user_id, username, antispam_time, reg_at):
    info = {
        "id": f"{user_id}",
        "username": f"{username}",
        "user_proxy":f"N/A",
        "dcr": "N/A",
        "dpk": "N/A",
        "dsk": "N/A",
        "amt": "N/A",
        "status": "FREE",
        "plan": f"N/A",
        "expiry": "N/A",
        "credit": "100",
        "antispam_time": f"{antispam_time}",
        "totalkey": "0",
        "reg_at": f"{reg_at}",
    }
    usersdb.insert_one(info)


@Client.on_message(filters.command("register", [".", "/"]))
async def cmd_register(Client, message):
    try:
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        antispam_time = int(time.time())
        yy, mm, dd = str(date.today()).split("-")
        reg_at = f"{dd}-{mm}-{yy}"
        find = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        registration_check = str(find)

        WELCOME_BUTTON = [
            [
                InlineKeyboardButton("Commands", callback_data="cmds")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        if registration_check == "None":
            await register_user(user_id, username, antispam_time, reg_at)
            resp = f"""<b>
Registration Successfull ♻️
━━━━━━━━━━━━━━
● Name: {message.from_user.first_name}
● User ID: {message.from_user.id}
● Role: Free
● Credits: 50

Message: You Got 50 Credits as a registration bonus . To Know Credits System /howcrd .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        else:
            resp = f"""<b>
Already Registered ⚠️

Message: You are already registered in our bot . No need to register now .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        await message.reply_text(resp, reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON))

    except Exception:
        import traceback
        await error_log(traceback.format_exc())


async def callback_register(Client, callback_query):
    try:
        user_id = str(callback_query.from_user.id)
        username = str(callback_query.from_user.username)
        antispam_time = int(time.time())
        yy, mm, dd = str(date.today()).split("-")
        reg_at = f"{dd}-{mm}-{yy}"
        find = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        registration_check = str(find)

        WELCOME_BUTTON = [
            [
                InlineKeyboardButton("Commands", callback_data="cmds")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        if registration_check == "None":
            await register_user(user_id, username, antispam_time, reg_at)
            resp = f"""<b>
Registration Successfull ♻️
━━━━━━━━━━━━━━
● Name: {callback_query.from_user.first_name}
● User ID: {user_id}
● Role: Free
● Credits: 50

Message: You Got 50 Credits as a registration bonus . To Know Credits System /howcrd .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        else:
            resp = f"""<b>
Already Registered ⚠️

Message: You are already registered in our bot . No need to register now .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        # Send the registration response as a new message instead of editing
        await callback_query.answer()
        await callback_query.edit_message_text(
            text=resp,
            reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON)
        )

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())


@Client.on_callback_query()
async def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "cmds":
        await CallbackQuery.answer()
        await callback_command(Client, CallbackQuery)

    if CallbackQuery.data == "register":
        await CallbackQuery.answer()
        await callback_register(Client, CallbackQuery)

    if CallbackQuery.data == "HOME":
        await CallbackQuery.answer()
        WELCOME_TEXT = f"""
<b>Hello User!

Hanuman  Checker Has plenty of Commands. We Have Auth Gates, Charge Gates, Tools, And Other Things.

Click Each of Them Below to Know Them Better.</b>
    """
        WELCOME_BUTTONS = [
            [
                InlineKeyboardButton("AUTH/B3/VBV", callback_data="AUTH"),
                InlineKeyboardButton("CHARGE", callback_data="CHARGE")
            ],
            [
                InlineKeyboardButton("TOOLS", callback_data="TOOLS"),
                InlineKeyboardButton("HELPER", callback_data="HELPER")
            ],
            [
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=WELCOME_TEXT,
            reply_markup=InlineKeyboardMarkup(WELCOME_BUTTONS))

    if CallbackQuery.data == "close":
        await CallbackQuery.answer()
        # Return to the start menu instead of deleting
        text = f"""
<b>🌟 Hello <a href="tg://user?id={CallbackQuery.from_user.id}">{CallbackQuery.from_user.first_name}</a>!</b>

<b>Welcome aboard the Hanuman  Checker! 🚀</b>

<b>I am your go-to bot, packed with a variety of gates, tools, and commands to enhance your experience. Excited to see what I can do?</b>

<b>👇 Tap the <i>Register</i> button to begin your journey.</b>
<b>👇 Discover my full capabilities by tapping the <i>Commands</i> button.</b>

"""
        WELCOME_BUTTON = [
            [
                InlineKeyboardButton("Register", callback_data="register"),
                InlineKeyboardButton("Commands", callback_data="cmds")
            ],
            [
                InlineKeyboardButton("Close", callback_data="delete")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON))

    if CallbackQuery.data == "delete":
        await CallbackQuery.answer()
        await CallbackQuery.message.delete()


    if CallbackQuery.data == "AUTH":
        AUTH_TEXT = f"""
<b>Hello User!

Hanuman  Checker  Auth Gates.

Click on each one below to get to know them better. .</b>
    """
        AUTH_BUTTONS = [
            [
                InlineKeyboardButton("Stripe Auth", callback_data="Auth2"),
                InlineKeyboardButton("Adyen Auth", callback_data="Adyen2"),
            ],
            [
                InlineKeyboardButton(
                    "Braintree B3", callback_data="BRAINTREEB3"),

                InlineKeyboardButton(
                    "Braintree VBV", callback_data="BRAINTREEVBV"),
            ],
            [
                InlineKeyboardButton("Back", callback_data="HOME"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=AUTH_TEXT,
            reply_markup=InlineKeyboardMarkup(AUTH_BUTTONS))
    if CallbackQuery.data == "Auth2":
        CHARGE_TEXT = """
🔹 Stripe Auth Gates of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Stripe Auth Options:
   1. Site-Based Auth:
      ➜ Single: /au cc|mm|yy|cvv ✅
      ➜ Mass: /mass cc|mm|yy|cvv ✅
      ➜ Txt: /autxt cc|mm|yy|cvv ✅


👤 Stripe Auth Options:
   1. Site-Based Auth:
      ➜ Single: /sau cc|mm|yy|cvv ✅
      ➜ Mass: /massau cc|mm|yy|cvv ✅
      ➜ Txt: /massautxt cc|mm|yy|cvv ✅


Total Auth Commands: 2

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="AUTH"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "Adyen2":
        CHARGE_TEXT = """
🔹 Adyen Auth Gates of Hanuman  Checker
🔹 Status: Inactive ✅️

🚀 Quick Commands Overview:

👤 Adyen Auth Options:
   1. Adyen Auth:
      ➜ Single: /ad cc|mm|yy|cvv ✅️
      ➜ Mass: /massad cc|mm|yy|cvv ✅️

Total Auth Commands: 1

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="AUTH"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "BRAINTREEVBV":
        CHARGE_TEXT = """
🔹 Braintree Gates of Goku  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Braintree VBV Options:
   1. VBV Lookup Gate:
      ➜ Single: /vbv cc|mm|yy|cvv ✅
      ➜ Mass (Limit=25): /mvbv cc|mm|yy|cvv ✅

Total Auth Commands: 1

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="AUTH"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )

    if CallbackQuery.data == "BRAINTREEB3":
        CHARGE_TEXT = """
🔹 Braintree B3 of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Braintree B3 Options:
   1. Braintree B3 Gate:
      ➜ Single: /b3 cc|mm|yy|cvv ✅
      ➜ Mass (Limit=5): /mb3 cc|mm|yy|cvv ✅

   2. Braintree B3 Gate:
      ➜ Single: /br cc|mm|yy|cvv ✅
      ➜ Mass (Limit=5): /mbr cc|mm|yy|cvv ✅      

Total Commands: 2

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="AUTH"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )





    if CallbackQuery.data == "CHARGE":
        CHARGE_TEXT = f"""
<b>Hello User!

Hanuman  Checker Charge Gates.

Click on each one below to get to know them better. .</b>
    """

        CHARGE_BUTTONS = [
            [
                InlineKeyboardButton("SK Based", callback_data="SKBASED"),
                InlineKeyboardButton("Braintree", callback_data="BRAINTREE"),
            ],
            [
                InlineKeyboardButton("Stripe Api", callback_data="SITE"),
                InlineKeyboardButton("Shopify", callback_data="SHOPIFY"),
            ],
            [
                InlineKeyboardButton("Paypal", callback_data="PAYPAL"),
            ],
            [
                InlineKeyboardButton("Back", callback_data="HOME"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTONS))
    if CallbackQuery.data == "PAYPAL":
        CHARGE_TEXT = """
🔹 PayPal Charge Gates of Hanuman  Checker
🔹 Status: ✅️ Inactive

🚀 Quick Commands Overview:

👤 PayPal Charge Options:
   1. PayPal Charge 0.1$:
      ➜ Single: /pp cc|mm|yy|cvv [ON] ✅️
      ➜ Mass: /mpp cc|mm|yy|cvv [ON] ✅️

   2. PayPal Charge 1.50$:
      ➜ Single: /py cc|mm|yy|cvv [OFF] ✅️
      ➜ Mass: /mpy cc|mm|yy|cvv [OFF] ✅️

Total Auth Commands: 2

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="CHARGE"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )  


    if CallbackQuery.data == "SKBASED":
        CHARGE_TEXT = """
🔹 Stripe Charge Gates of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Stripe Charge Options:
   1. SK BASED CHARGE 0.5$ CVV:
      ➜ Single: /svv cc|mm|yy|cvv ✅
      ➜ Mass: /msvv cc|mm|yy|cvv ✅
      ➜ Mass txt (Limit=3k): /svvtxt [in reply to file] ✅
      ➜ Self SK also added, check: /selfcmd ✅

   2. SK BASED 0.5$ CCN CHARGE:
      ➜ Single: /ccn cc|mm|yy|cvv ✅
      ➜ Mass: /mccn cc|mm|yy|cvv ✅
      ➜ Mass txt (Limit=3k): /ccntxt [in reply to file] ✅
      ➜ Self SK also added, check: /selfcmd ✅

   3. SK BASED 0.5$ CVV CHARGE:
      ➜ Single: /cvv cc|mm|yy|cvv ✅
      ➜ Mass: /mcvv cc|mm|yy|cvv ✅
      ➜ Mass txt (Limit=3k): /cvvtxt [in reply to file] ✅
      ➜ Self SK also added, check: /selfcmd ✅

Total Charge Commands: 3

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="CHARGE"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "SITE":
        CHARGE_TEXT = """
🔹 Site Charge Gates of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Site Charge Options:
   1. SITEBASE 1$ CVV CHARGE:
      ➜ Single: /chk cc|mm|yy|cvv ✅
      ➜ Mass: /mchk cc|mm|yy|cvv ✅


   2. SITEBASE 1$ CVV CHARGE:
      ➜ Single: /st cc|mm|yy|cvv ✅
      ➜ Mass: /mst cc|mm|yy|cvv ✅


Total Charge Commands: 2

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="CHARGE"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "BRAINTREE":
        CHARGE_TEXT = """
🔹 Braintree Charge Gates of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Braintree Charge Options:
   1. Braintree Charge 1£:
      ➜ Single: /br cc|mm|yy|cvv ✅
      ➜ Mass: /mbr cc|mm|yy|cvv ✅

Total Auth Commands: 1

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="CHARGE"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "SHOPIFY":
        CHARGE_TEXT = """

🔹 Shopify Charge Gates of Hanuman Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Shopify Charge Options:
   1. Shopify Charge 10$:
      ➜ Single: /sh cc|mm|yy|cvv ✅
      ➜ Mass: /msh cc|mm|yy|cvv ✅

   2. Shopify Charge 27.51$:
      ➜ Single: /so cc|mm|yy|cvv ✅
      ➜ Mass: /mso cc|mm|yy|cvv ✅

   3. Shopify Charge 20$:
      ➜ Single: /sho cc|mm|yy|cvv ✅
      ➜ Mass: /msho cc|mm|yy|cvv ✅

   4. Shopify Charge 20$:
      ➜ Single: /sg cc|mm|yy|cvv ✅
      ➜ Mass: /msg cc|mm|yy|cvv ✅

Total Auth Commands: 4

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="CHARGE"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )

    if CallbackQuery.data == "HELPER":
        HELPER_TEXT = """
🔹 Helper Commands of Hanuman Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Helper Options:
   1. User Information: /info - Check your account details ✅
   2. Credit System: /howcrd - Learn about credit system ✅
   3. Group Authorization: /howgp - How to add bot to groups ✅
   4. Premium Plans: /buy - View premium plans ✅
   5. User ID: /id - Get your user ID ✅
   6. Bot Status: /ping - Check bot response time ✅

Total Helper Commands: 6

"""
        HELPER_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="HOME"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=HELPER_TEXT,
            reply_markup=InlineKeyboardMarkup(HELPER_BUTTON)
        )

    if CallbackQuery.data == "SCRAPPER":
        SCRAPPER_TEXT = """
🔹 Scrapper Tools of Hanuman Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Scraper Tools:
   1. CC Scraper Gate: /scr channel_username 100 ✅ (Limit: 5K)
   2. Bin Based CC Scraper Gate: /scrbin 440393 channel_username 100 ✅ (Limit: 5K)
   3. SK Scraper Gate: /scrsk channel_username 100 ✅ (Limit: 5K)

Total Scraper Commands: 3

"""
        SCRAPPER_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="TOOLS"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=SCRAPPER_TEXT,
            reply_markup=InlineKeyboardMarkup(SCRAPPER_BUTTON)
        )

    if CallbackQuery.data == "GENERATORTOOLS":
        GENERATOR_TEXT = """
🔹 Generator Tools of Hanuman Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Generator Tools:
   1. CC Generator: /gen 447697 ✅ (Generate random cards)
   2. CC Generator with Amount: /gen 447697 100 ✅ (Specify amount)
   3. CC Generator with Details: /gen 447697|12|23|000 ✅ (With expiry & CVV)
   4. Fake Identity Generator: /fake ✅ (Generate fake person details)

Total Generator Commands: 4

"""
        GENERATOR_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="TOOLS"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=GENERATOR_TEXT,
            reply_markup=InlineKeyboardMarkup(GENERATOR_BUTTON)
        )

    if CallbackQuery.data == "BINANDOTHERS":
        BINTOOLS_TEXT = """
🔹 Bin & Other Tools of Hanuman Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Bin & Other Tools:
   1. BIN Lookup: /bin 447697 ✅ (Check BIN details)
   2. IP Lookup: /ip 8.8.8.8 ✅ (Check IP information)
   3. Gateway Finder: /url site.com ✅ (Find payment gateways)
   4. SK to PK Converter: /pk sk_live_xxx ✅ (Convert SK to PK)
   5. SK Info Checker: /skinfo sk_live_xxx ✅ (Check SK details)
   6. SK User Checker: /skuser sk_live_xxx ✅ (Check SK user info)

Total Bin & Other Commands: 6

"""
        BINTOOLS_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="TOOLS"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=BINTOOLS_TEXT,
            reply_markup=InlineKeyboardMarkup(BINTOOLS_BUTTON)
        )
    if CallbackQuery.data == "TOOLS":
        TOOLS_TEXT = f"""
<b>Hello User!

Hanuman  Checker Tools.

Click on each one below to get to know them better..</b>
    """
        CHARGE_BUTTONS = [
            [
                InlineKeyboardButton("Scrapper", callback_data="SCRAPPER"),
                InlineKeyboardButton("SK TOOLS", callback_data="SKSTOOL"),
            ],
            [
                InlineKeyboardButton(
                    "Genarator", callback_data="GENARATORTOOLS"),
                InlineKeyboardButton(
                    "Bin & Others", callback_data="BINANDOTHERS"),
            ],
            [
                InlineKeyboardButton("Back", callback_data="HOME"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=TOOLS_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTONS))

    if CallbackQuery.data == "SKSTOOL":
        CHARGE_TEXT = """
🔹 SK Tools of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 SK Tools:
   1. SK Key Checker Gate: /sk sk_live_xxxxxx ✅ (Limit: Single)
   2. SK To PK Generator Gate: /pk sk_live_xxxxxx ✅ (Limit: Single)
   3. SK User Checker Gate: /skuser sk_live_xxxxxx ✅ (Limit: Single)
   4. SK Info Checker Gate: /skinfo sk_live_xxxxxx ✅ (Limit: Single)

Total Auth Commands: 4

"""
        CHARGE_BUTTON = [
            [
                InlineKeyboardButton("Back", callback_data="TOOLS"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        await CallbackQuery.edit_message_text(
            text=CHARGE_TEXT,
            reply_markup=InlineKeyboardMarkup(CHARGE_BUTTON)
        )
    if CallbackQuery.data == "SCRAPPER":
        CHARGE_TEXT = """
🔹 Scrapper Tools Gates of Hanuman  Checker
🔹 Status: ✅ Active

🚀 Quick Commands Overview:

👤 Scraper Tools:
   1. CC Scraper Gate: /scr channel_username 100 ✅ (Limit: 5K)
   2. Bin Based CC Scraper Gate: /scrbin 440393 channel_username 100 ✅ (Limit: 5K)
   3. SK Scraper Gate: /scrsk channel_username 100 ✅ (Limit: 5K)

Total Scraper Commands: 3

"""