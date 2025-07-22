import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

# Your Telegram Bot Token from BotFather
BOT_TOKEN = os.getenv("7786508141:AAETbqJgSE7DI8QuCs7KT5GYx9ZqtI54W2c")

# Your numeric Telegram User ID
# The default value 0 is a safeguard in case the variable is not set
ADMIN_ID = int(os.getenv("6246979600", 0))

# The URL for the webhook, provided by the deployment platform (like Render)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# The port number for the webhook to listen on
PORT = int(os.getenv("PORT", 8443))

# Player data file name
PLAYER_DATA_FILE = "ashenfall_player_data_fa.json"

