from telegram import Update
from telegram.ext import ContextTypes
from data_manager import PlayerData

_player_data = None
def set_data_manager(data_manager: PlayerData):
    global _player_data
    _player_data = data_manager

async def say_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return

    if not context.args:
        await update.message.reply_text("چه بگویی؟")
        return
    
    message = " ".join(context.args)
    await update.message.reply_text(f"تو می‌گویی: «{message}»")

    players_in_room = _player_data.get_players_in_room(player['location'])
    for pid in players_in_room:
        if str(pid) != str(user_id):
            await context.bot.send_message(chat_id=pid, text=f"*{player['username']} می‌گوید:* «{message}»", parse_mode='Markdown')

async def emote_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return

    if not context.args:
        await update.message.reply_text("چه حالتی؟ مثال: `/حالت به آرامی سر تکان می‌دهد.`")
        return
        
    action = " ".join(context.args)
    full_emote = f"_{player['username']} {action}_"
    await update.message.reply_text(full_emote, parse_mode='Markdown')

    players_in_room = _player_data.get_players_in_room(player['location'])
    for pid in players_in_room:
        if str(pid) != str(user_id):
            await context.bot.send_message(chat_id=pid, text=full_emote, parse_mode='Markdown')

async def bonds_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    player = _player_data.get_player(user_id)
    if not player: return

    bonds = player.get('bonds', {})
    if not bonds:
        await update.message.reply_text("تو هنوز هیچ رابطه عمیقی با کسی در این شهر نداری.")
        return

    response = ["*روابط تو:*\n"]
    for target_id, bond_data in bonds.items():
        target_player = _player_data.get_player(target_id)
        if target_player:
            target_name = target_player['username']
            bond_type = bond_data.get('type', 'ناشناخته')
            bond_value = bond_data.get('value', 0)
            response.append(f"- *{target_name}*: {bond_type} ({bond_value})")
    
    await update.message.reply_text("\n".join(response), parse_mode='Markdown')
