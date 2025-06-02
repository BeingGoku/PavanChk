
from pyrogram import Client
from replit.object_storage import Client as StorageClient
import json
import os

def download_and_upload_video():
    """Download video from Telegram and upload to Object Storage"""
    try:
        # Load config
        with open("FILES/config.json", "r", encoding="utf-8") as f:
            DATA = json.load(f)
            API_ID = DATA["API_ID"]
            API_HASH = DATA["API_HASH"]
            BOT_TOKEN = DATA["BOT_TOKEN"]

        # Create Telegram client
        app = Client("video_downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
        
        with app:
            # Replace these with your actual values from the Telegram link
            chat_username = "YouBeingNaruto"  # From your link
            message_id = 5  # From your link
            
            try:
                # Get the message
                message = app.get_messages(chat_username, message_id)
                
                if message.video:
                    print("Downloading video...")
                    # Download the video
                    file_path = app.download_media(message, file_name="start_video.mp4")
                    print(f"Video downloaded to: {file_path}")
                    
                    # Upload to Object Storage
                    storage_client = StorageClient()
                    
                    with open(file_path, 'rb') as video_file:
                        storage_client.upload_from_file("start_video.mp4", video_file)
                    
                    # Get download URL
                    download_url = storage_client.download_url("start_video.mp4")
                    
                    print(f"Video uploaded successfully!")
                    print(f"Object Storage URL: {download_url}")
                    print("\nNow update your start command with this URL:")
                    print(f'video="{download_url}"')
                    
                    # Clean up local file
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    
                    return download_url
                    
                else:
                    print("No video found in the message")
                    return None
                    
            except Exception as e:
                print(f"Error accessing message: {e}")
                print("Make sure the bot has access to the channel/chat")
                return None
                
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    download_and_upload_video()
