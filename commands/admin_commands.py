from telegram import Update
from telegram.ext import ContextTypes
from data_manager import PlayerData
from game_world import GAME_MAP
import config

_player_data = None
def set_data_manager(data_manager: PlayerData):
    global _player_data
    _player_data = data_manager

async def check_admin(update: Update) -> bool:
    """Checks if the user is the admin."""
    if update.effective_user.id != config.ADMIN_ID:
        await update.message.reply_text("قدرتی غریب، دید تو را مسدود می‌کند.")
        return False
    return True

async def gaze_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_admin(update): return

    if not context.args:
        await update.message.reply_text("فرمان الهی: `/نگاه_الهی <نام_بازیکن>`")
        return

    target_name = context.args[0]
    target_id, target_player = _player_data.get_player_by_name(target_name)
    
    if not target_player:
        await update.message.reply_text(f"نگاه تو هیچ فانی‌ای به نام «{target_name}» را نمی‌یابد.")
        return

    loc = GAME_MAP[target_player['location']]['name']
    stats_text = (
        f"👁️ *نگاه تو بر {target_player['username']} فرود می‌آید*\n\n"
        f"*شناسه:* `{target_id}`\n"
        f"*مکان:* {loc}"
    )
    await update.message.reply_text(stats_text, parse_mode='Markdown')

async def whisper_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_admin(update): return

    if len(context.args) < 2:
        await update.message.reply_text("فرمان الهی: `/نجوا <نام_بازیکن> <پیام>`")
        return
    
    target_name = context.args[0]
    message = " ".join(context.args[1:])
    target_id, _ = _player_data.get_player_by_name(target_name)
            
    if not target_id:
        await update.message.reply_text(f"نجوای تو هیچ فانی‌ای به نام «{target_name}» را نمی‌یابد.")
        return
        
    try:
        whisper_text = f"_فکری غریب به ذهنت خطور می‌کند، نجوایی در باد: «{message}»_"
        await context.bot.send_message(chat_id=int(target_id), text=whisper_text, parse_mode='Markdown')
        await update.message.reply_text(f"تو به {target_name} نجوا کردی.")
    except Exception as e:
        await update.message.reply_text(f"نجوای تو در پوچی گم شد. (خطا: {e})")

async def bestow_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_admin(update): return
        
    if len(context.args) < 2:
        await update.message.reply_text("فرمان الهی: `/عطا <نام_بازیکن> <نام_آیتم_با_خط_زیر>`")
        return
        
    target_name = context.args[0]
    item_name = " ".join(context.args[1:]).replace("_", " ")
    target_id, target_player = _player_data.get_player_by_name(target_name)

    if not target_player:
        await update.message.reply_text(f"هدیه تو هیچ فانی‌ای به نام «{target_name}» را نمی‌یابد.")
        return

    target_player['inventory'].append(item_name)
    _player_data.save_data()
    
    try:
        bestow_text = f"_همانطور که دست در جیبت می‌کنی، انگشتانت به چیزی جدید برخورد می‌کند. تو یک *{item_name}* بیرون می‌آوری!_"
        await context.bot.send_message(chat_id=int(target_id), text=bestow_text, parse_mode='Markdown')
        await update.message.reply_text(f"تو «{item_name}» را به {target_name} عطا کردی.")
    except Exception as e:
        await update.message.reply_text(f"هدیه تو در مه محو شد. (خطا: {e})")
