# Copyright (C) 2019 Nahuel Gomez Castro <nahual_gomca@outlook.com.ar>
#
# This file is part of Animux bot.
#
# Animux bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Animux bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List

from telegram import Bot, ChatAction, ParseMode, Update
from telegram.ext import CommandHandler, Filters, run_async

from animux_bot import DISPATCHER, LOGGER
from .helper_funcs.chat_status import (bot_can_restrict,
                                       is_user_ban_protected,
                                       user_can_restrict)
from .helper_funcs.extraction import extract_user_and_text


@run_async
@bot_can_restrict
@user_can_restrict
def ban(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat
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

DISPATCHER.add_handler(BAN_COMMAND_HANDLER)
