from typing import List

from telegram import Bot, ChatAction, Update, ParseMode
from telegram.ext import CommandHandler, Filters, run_async

from pony_bot import LOGGER, dispatcher
from pony_bot.modules.helper_funcs.chat_status import (bot_can_restrict,
                                                       is_user_ban_protected,
                                                       user_can_restrict)
from pony_bot.modules.helper_funcs.extraction import extract_user_and_text


@run_async
@bot_can_restrict
@user_can_restrict
def ban(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        bot.send_chat_action(chat.id, ChatAction.TYPING)
        message.reply_text('Uhm? No sé a quien quieres que banee.')
        return

    if user_id == bot.id:
        bot.send_chat_action(chat.id, ChatAction.TYPING)
        message.reply_text('Hey! Esa soy yo! (O.O)')
        bot.send_sticker(chat.id, 'CAADAgADrRsAAuCjgge1g6be76IiHgI')
        return

    if is_user_ban_protected(chat, user_id):
        bot.send_chat_action(chat.id, ChatAction.TYPING)
        message.reply_text('Etto... No puedo banear administradores (⌒_⌒;)')
        return

    chat.kick_member(user_id)
    bot.send_sticker(chat.id, 'CAADAgADpxsAAuCjggf0_Fu4xLzgxAI')
    bot.send_chat_action(chat.id, ChatAction.TYPING)
    message.reply_text('¡Banead@!')
    LOGGER.info('Usuario %s baneado del grupo %s' % (user_id, chat.title))

    bot.send_sticker(user_id, 'CAADAgADpxsAAuCjggf0_Fu4xLzgxAI')
    bot.send_chat_action(user_id, ChatAction.TYPING)
    bot.send_message(user_id, 'Te he baneado del grupo *%s*\n\nRazón: %s' %
                     (chat.title, reason or 'Sin especificar'), ParseMode.MARKDOWN)


# Info about the module
__mod_name__ = 'Bans'


# Load commands
BAN_COMMAND_HANDLER = CommandHandler('ban', ban, Filters.group, pass_args=True)

dispatcher.add_handler(BAN_COMMAND_HANDLER)
