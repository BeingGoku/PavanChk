import httpx
import asyncio
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
import urllib.parse


# Fetch GPT response using Gemini API
async def fetch_response(prompt):
    # URL encode the prompt for the query parameter
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://nggemini.tiiny.io/?prompt={encoded_prompt}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            
            # Parse JSON response and extract text content
            try:
                json_response = response.json()
                if "candidates" in json_response and len(json_response["candidates"]) > 0:
                    candidate = json_response["candidates"][0]
                    if "content" in candidate and "parts" in candidate["content"]:
                        parts = candidate["content"]["parts"]
                        if len(parts) > 0 and "text" in parts[0]:
                            return parts[0]["text"].strip()
                
                # Fallback if JSON structure is different
                return "Unable to parse response from API"
            except:
                # If it's not JSON, return as plain text
                return response.text
                
        except httpx.ReadTimeout:
            raise TimeoutError("The Gemini API request timed out.")
        except Exception as e:
            raise RuntimeError(f"API Error: {e}")


# GPT Command Handler
@Client.on_message(filters.command("gpt", [".", "/"]))
async def cmd_gpt(client, message):
    try:
        checkall = await check_all_thing(client, message)
        if not checkall[0]:
            return

        role = checkall[1]

        # Extract prompt
        if message.reply_to_message and message.reply_to_message.text:
            prompt = message.reply_to_message.text
        else:
            try:
                prompt = message.text.split(" ", 1)[1]
            except IndexError:
                await message.reply_text(
                    "<b>Invalid Prompt ⚠️</b>\n\nMessage: No valid prompt provided."
                )
                return

        # Indicate processing
        processing_message = await message.reply_text("⌛️ Answering...")

        # Retry logic for API call
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = await fetch_response(prompt)
                break
            except TimeoutError:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            except Exception as e:
                import traceback
                await error_log(traceback.format_exc())
                await processing_message.edit_text(
                    "⚠️ Failed to generate a response. Please try again later."
                )
                return
        else:
            await processing_message.edit_text(
                "⚠️ Timeout: The request took too long to process."
            )
            return

        # Add footer to response
        footer = "\n\n☀️ BOT BY - <a href=\"https://t.me/lord_hanumant_bot\">Hanuman</a>\n"
        final_response = f"{response}{footer}"
        
        # Send response
        await processing_message.edit_text(f"<b>{final_response}</b>")

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(
            "⚠️ An unexpected error occurred. Please try again later."
        )