from pyrogram.client import Client
import json
from FUNC.server_stats import send_server_alert
from web_server import start_web_server

plugins = dict(root="BOT")

with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
    API_ID    = DATA["API_ID"]
    API_HASH  = DATA["API_HASH"]
    BOT_TOKEN = DATA["BOT_TOKEN"]

# Load phone number from config for user session
PHONE_NUMBER = DATA["PHONE_NUMBER"]

user = Client( 
            "Scrapper", 
             api_id   = API_ID, 
             api_hash = API_HASH,
             phone_number = PHONE_NUMBER
              )

bot = Client(
    "MY_BOT", 
    api_id    = API_ID, 
    api_hash  = API_HASH, 
    bot_token = BOT_TOKEN, 
    plugins   = plugins 
)

if __name__ == "__main__":
    # send_server_alert()
    print("Bot Starting...")
    
    # Start web server for UptimeRobot monitoring
    start_web_server()

    try:
        bot.run()
        print("Bot Active ✅")
    except Exception as e:
        print(f"Error: {e}")
        # Handle database locked error
        if "database is locked" in str(e).lower():
            print("Database locked error detected. Cleaning session files...")
            import os
            import time
            try:
                # Close any existing connections
                try:
                    bot.stop()
                    user.stop()
                except:
                    pass
                
                # Wait a moment for file handles to release
                time.sleep(2)
                
                # Remove session files
                session_files = [
                    "MY_BOT.session",
                    "MY_BOT.session-journal", 
                    "MY_BOT.session-shm",
                    "MY_BOT.session-wal",
                    "Scrapper.session",
                    "Scrapper.session-journal",
                    "Scrapper.session-shm", 
                    "Scrapper.session-wal"
                ]
                
                for file in session_files:
                    if os.path.exists(file):
                        os.remove(file)
                        print(f"Removed {file}")
                
                print("Session files cleaned. Please restart the bot.")
            except Exception as cleanup_error:
                print(f"Error cleaning session files: {cleanup_error}")
        
        # If session is revoked, remove session files and try again
        elif "SESSION_REVOKED" in str(e) or "AUTH_KEY_UNREGISTERED" in str(e):
            print("Session revoked or unregistered. Cleaning session files...")
            import os
            try:
                if os.path.exists("MY_BOT.session"):
                    os.remove("MY_BOT.session")
                if os.path.exists("MY_BOT.session-journal"):
                    os.remove("MY_BOT.session-journal")
                if os.path.exists("Scrapper.session"):
                    os.remove("Scrapper.session")
                if os.path.exists("Scrapper.session-journal"):
                    os.remove("Scrapper.session-journal")
                print("Session files removed. Please restart the bot to re-authenticate.")
            except Exception as cleanup_error:
                print(f"Error cleaning session files: {cleanup_error}")
        else:
            print("An unexpected error occurred.")