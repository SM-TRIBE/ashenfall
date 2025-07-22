import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

# Your Telegram Bot Token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Your numeric Telegram User ID
# The default value 0 is a safeguard in case the variable is not set
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# The URL for the webhook, provided by the deployment platform (like Render)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# The port number for the webhook to listen on
PORT = int(os.getenv("PORT", 8443))

# Player data file name
PLAYER_DATA_FILE = "ashenfall_player_data_fa.json"

