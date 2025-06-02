
import json
from pyrogram import Client

# Load config
with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
    API_ID = DATA["API_ID"]
    API_HASH = DATA["API_HASH"]
    PHONE_NUMBER = DATA["PHONE_NUMBER"]

# Create user client
user = Client(
    "Scrapper",
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=PHONE_NUMBER
)

print("Starting authentication process...")
print(f"Phone number from config: {PHONE_NUMBER}")

# Start the client to authenticate
with user:
    print("Authentication successful!")
    print("Session file created: Scrapper.session")
    print("You can now use the scrapper commands.")
