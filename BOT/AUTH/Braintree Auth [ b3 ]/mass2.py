import json
import time
import threading
import asyncio
import httpx
from pyrogram import Client, filters
from datetime import timedelta
from FUNC.usersdb_func import *
from FUNC.defs import *  # Import all functions from defs.py
from .gate2 import *
from .response import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_mass import *


async def mchkfunc(fullcc, user_id):
    retries = 3
    for attempt in range(retries):
        try:
            proxies = await get_proxy_format()
            proxy_url = proxies["https://"]  # Use the HTTPS proxy URL
            transport = httpx.AsyncHTTPTransport(proxy=proxy_url)
            session = httpx.AsyncClient(
                timeout=30, transport=transport, follow_redirects=True)
            result = await create_braintree_auth(fullcc, session)
            getresp = await get_charge_resp(result, user_id, fullcc)
            response = getresp["response"]
            status   = getresp["status"]

            await session.aclose()
            return f"Card↯ <code>{fullcc}</code>\n<b>Status - {status}</b>\n<b>Result -⤿ {response} ⤾</b>\n\n"

        except Exception as e:
            import traceback
            await error_log(traceback.format_exc())
            if attempt < retries - 1:
                await asyncio.sleep(0.5)
                continue
            else:
                return f"<code>{fullcc}</code>\n<b>Result - DECLINED ❌</b>\n"


@Client.on_message(filters.command("mbr", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_auth_cmd(Client, message))
    loop.close()


async def stripe_mass_auth_cmd(Client, message):
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall = await check_all_thing(Client, message)

        if checkall[0] == False:
            return

        role = checkall[1]
        getcc = await getcc_for_mass(message, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return
        
        ccs = getcc[1]

        if role != "OWNER":
            if len(ccs) > 5:
                resp = """<b>
Limit Reached ⚠️

Message: You can't check more than 5 CCs at a time.
                </b>"""
                await message.reply_text(resp)
                return

        resp = f"""
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -  Braintree Auth

- 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭 -{len(ccs)}
- 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - Checking CC For {first_name}

- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️
"""
        nov = await message.reply_text(resp, message.id)

        amt = 0
        start = time.perf_counter()
        works = [mchkfunc(i, user_id) for i in ccs]
        worker_num = int(json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["THREADS"])

        # Store all results
        all_results = []
        current_chunk = []
        
        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                amt += 1
                all_results.append(i)
                current_chunk.append(i)
                
                # Send results in smaller chunks of 3
                if len(current_chunk) >= 3:
                    try:
                        chunk_text = "".join(current_chunk)
                        await message.reply_text(chunk_text)
                        current_chunk = []
                    except:
                        pass
            await asyncio.sleep(1)
            works = works[worker_num:]

        # Send any remaining results
        if current_chunk:
            try:
                chunk_text = "".join(current_chunk)
                await message.reply_text(chunk_text)
            except:
                pass

        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)
        sec = int(seconds)

        # Send the final time message
        time_text = f"""
<b>↯ Mass Braintree Auth Results</b>
- 𝗧𝗶𝗺𝗲 -  {hour}.h {min}.m {sec}.s 
- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐚𝐫𝐝𝐬 - {len(ccs)}
"""
        await message.reply_text(time_text)
        
        await massdeductcredit(user_id, len(ccs))
        await setantispamtime(user_id)

    except:
        import traceback
        await error_log(traceback.format_exc())
