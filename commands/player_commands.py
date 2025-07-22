from telegram import Update
from telegram.ext import ContextTypes
from data_manager import PlayerData
from game_world import GAME_MAP

# This function will be called by the main bot to set the data_manager instance
_player_data = None
def set_data_manager(data_manager: PlayerData):
    global _player_data
    _player_data = data_manager

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    is_new = _player_data.create_player(user.id, user.first_name)

    if is_new:
        welcome_text = (
            f"خوش آمدی، {user.first_name}، به دنیای *خاکستران: تاج شکسته*.\n\n"
            "دوک مرده است. شهر در خونریزی است. در این عصر هرج‌ومرج، تو با هیچ‌چیز جز هوش و لباس‌های کهنه‌ات از خواب بیدار می‌شوی.\n\n"
            "--- *دستورات اصلی* ---\n"
            "`/نگاه` - اطراف خود را ببین.\n"
            "`/حرکت <جهت>` - به مکانی جدید برو.\n"
_player_data = None
def set_data_manager(data_manager: PlayerData):
    global _player_data
    _player_data = data_manager

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    is_new = _player_data.create_player(user.id, user.first_name)

    if is_new:
        welcome_text = (
            f"خوش آمدی، {user.first_name}، به دنیای *خاکستران: تاج شکسته*.\n\n"
            "دوک مرده است. شهر در خونریزی است. در این عصر هرج‌ومرج، تو با هیچ‌چیز جز هوش و لباس‌های کهنه‌ات از خواب بیدار می‌شوی.\n\n"
            "--- *دستورات اصلی* ---\n"
            "`/نگاه` - اطراف خود را ببین.\n"
            "`/حرکت <جهت>` - به مکانی جدید برو.\n"
            "`/وضعیت` - مشخصات شخصیت خود را ببین.\n"
            "`/دارایی` - محتویات کوله‌پشتی خود را ببین.\n"
            "--------------------------\n\n"
            "سفر تو اکنون آغاز می‌شود."
        )
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
        await look_command(update, context)
    else:
        await update.message.reply_text(f"به خاکستران خوش برگشتی، {user.first_name}.")
        await look_command(update, context)

async def look_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player:
        await update.message.reply_text("ابتدا باید با دستور /شروع سفر خود را آغاز کنی.")
        return

    location_id = player['location']
    location = GAME_MAP.get(location_id)
    if not location:
        await update.message.reply_text("خطا: مکان نامعتبر.")
        return

    players_in_room = _player_data.get_players_in_room(location_id)
    other_player_names = [p['username'] for pid, p in players_in_room.items() if str(pid) != str(user_id)]
    
    others_text = ""
    if other_player_names:
        others_text = "\n\n_همچنین اینجا: " + "، ".join(other_player_names) + "_"

    exits = "، ".join(location['exits'].keys())
    response_text = (
        f"*📍 {location['name']}*\n\n"
        f"{location['desc']}\n\n"
        f"خروجی‌ها: `{exits}`"
        f"{others_text}"
    )
    await update.message.reply_text(response_text, parse_mode='Markdown')

async def move_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return

    if not context.args:
        await update.message.reply_text("به کجا حرکت می‌کنی؟ امتحان کن: `/حرکت <جهت>`.")
        return

    direction = context.args[0].lower()
    current_location = GAME_MAP.get(player['location'])

    if direction in current_location['exits']:
        # Notify others
        players_in_room = _player_data.get_players_in_room(player['location'])
        for pid in players_in_room:
            if str(pid) != str(user_id):
                await context.bot.send_message(chat_id=pid, text=f"_{player['username']} به سمت {direction} می‌رود._", parse_mode='Markdown')

        new_location_id = current_location['exits'][direction]
        player['location'] = new_location_id
        _player_data.save_data()
        
        # Notify new room
        new_players_in_room = _player_data.get_players_in_room(new_location_id)
        for pid in new_players_in_room:
            if str(pid) != str(user_id):
                 await context.bot.send_message(chat_id=pid, text=f"_{player['username']} از راه می‌رسد._", parse_mode='Markdown')

        await look_command(update, context)
    else:
        await update.message.reply_text("نمی‌توانی از آن طرف بروی.")

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return

    attrs = "\n".join([f"  - {k}: {v}" for k, v in player['attributes'].items()])
    skills = "\n".join([f"  - {k}: {v}" for k, v in player['skills'].items()])
    faction_name = player.get('faction') or "ندارد"
    
    stats_text = (
        f"👤 *شخصیت: {player['username']}*\n\n"
        f"*جناح:* {faction_name}\n\n"
        f"*ویژگی‌ها:*\n{attrs}\n\n"
        f"*مهارت‌ها:*\n{skills}"
    )
    await update.message.reply_text(stats_text, parse_mode='Markdown')

async def inventory_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return
    
    if not player['inventory']:
        inv_text = "کوله‌پشتی تو خالی است."
    else:
        inv_text = "محتویات کوله‌پشتی تو:\n- " + "\n- ".join(player['inventory'])
        
    await update.message.reply_text(inv_text)
