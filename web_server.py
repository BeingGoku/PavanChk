
from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running! ✅", 200

@app.route('/status')
def status():
    return {
        "status": "online",
        "timestamp": time.time(),
        "message": "HANUMAN Checker Bot is active"
    }, 200

def run_web_server():
    app.run(host='0.0.0.0', port=8000, debug=False)

def start_web_server():
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    print("Web server started on port 8000 for UptimeRobot monitoring")
