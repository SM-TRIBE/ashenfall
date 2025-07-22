import logging
import config
from telegram.ext import Application, CommandHandler
from data_manager import PlayerData

# Import command modules
from commands import player_commands, social_commands, admin_commands

# --- Logging Setup ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    if not config.BOT_TOKEN:
        logger.error("FATAL: BOT_TOKEN is not configured. Please set it in your .env file or environment variables.")
        return

    # --- Initialization ---
    application = Application.builder().token(config.BOT_TOKEN).build()
    
    # Initialize the data manager
    player_data_manager = PlayerData(config.PLAYER_DATA_FILE)

    # Set the data manager instance for all command modules
    player_commands.set_data_manager(player_data_manager)
    social_commands.set_data_manager(player_data_manager)
    admin_commands.set_data_manager(player_data_manager)

    # --- Command Handlers ---
    # Player Commands
    application.add_handler(CommandHandler(["start", "شروع"], player_commands.start_command))
    application.add_handler(CommandHandler(["look", "نگاه"], player_commands.look_command))
    application.add_handler(CommandHandler(["move", "حرکت"], player_commands.move_command))
    application.add_handler(CommandHandler(["stats", "وضعیت"], player_commands.stats_command))
    application.add_handler(CommandHandler(["inventory", "دارایی"], player_commands.inventory_command))
    
    # Social Commands
    application.add_handler(CommandHandler(["say", "بگو"], social_commands.say_command))
    application.add_handler(CommandHandler(["emote", "حالت"], social_commands.emote_command))
    application.add_handler(CommandHandler(["bonds", "روابط"], social_commands.bonds_command))

    # Admin Commands
    application.add_handler(CommandHandler(["gaze", "نگاه_الهی"], admin_commands.gaze_command))
    application.add_handler(CommandHandler(["whisper", "نجوا"], admin_commands.whisper_command))
    application.add_handler(CommandHandler(["bestow", "عطا"], admin_commands.bestow_command))

    # --- Run the Bot ---
    if config.WEBHOOK_URL:
        # Run bot in webhook mode for deployment
        logger.info(f"Starting bot in webhook mode. Listening on port {config.PORT}")
        application.run_webhook(
            listen="0.0.0.0",
            port=config.PORT,
            url_path=config.BOT_TOKEN,
            webhook_url=f"{config.WEBHOOK_URL}/{config.BOT_TOKEN}"
        )
    else:
        # Run bot in polling mode for local development
        logger.info("Starting bot in polling mode.")
        application.run_polling()

if __name__ == "__main__":
    main()
