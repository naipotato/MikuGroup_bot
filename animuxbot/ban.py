# -*- coding: utf-8 -*-
#
# ban.py - This file is part of animux-bot
#
# Copyright (C) 2018 Nahuel Gomez Castro <nahual_gomca@outlook.com.ar>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from telegram import ChatAction, ChatMember


def ban(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Uhm? No puedo banear a nadie si no respondes a un mensaje')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Lo siento, pero me dijeron que tú no puedes banear usuarios...')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... no tengo los permisos para banear usuarios (╥_╥)')
        return

    if update.message.reply_to_message.forward_from is not None:
        user = update.message.reply_to_message.forward_from
    else:
        user = update.message.reply_to_message.from_user

    if user == bot.get_me():
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Hey! Esa soy yo! (O.O)')
        bot.send_sticker(update.message.chat.id,
                         'CAADAgADrRsAAuCjgge1g6be76IiHgI')
        return

    if update.message.reply_to_message.forward_from is not None:
        chat_member = bot.get_chat_member(
            update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        chat_member = bot.get_chat_member(
            update.message.chat.id, update.message.reply_to_message.from_user.id)

    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... No puedo banear administradores (⌒_⌒;)')
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.kick_chat_member(update.message.chat.id,
                             update.message.reply_to_message.forward_from.id)
    else:
        bot.kick_chat_member(update.message.chat.id,
                             update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text('¡Banead@!')
    bot.send_sticker(update.message.chat.id, 'CAADAgADpxsAAuCjggf0_Fu4xLzgxAI')


def kick(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Uhm? No puedo expulsar a nadie si no respondes a un mensaje')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Lo siento, pero me dijeron que tú no puedes expulsar usuarios...')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... no tengo los permisos para expulsar usuarios (╥_╥)')
        return

    if update.message.reply_to_message.forward_from is not None:
        user = update.message.reply_to_message.forward_from
    else:
        user = update.message.reply_to_message.from_user

    if user == bot.get_me():
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Hey! Esa soy yo! (O.O)')
        bot.send_sticker(update.message.chat.id,
                         'CAADAgADrRsAAuCjgge1g6be76IiHgI')
        return

    if update.message.reply_to_message.forward_from is not None:
        chat_member = bot.get_chat_member(
            update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        chat_member = bot.get_chat_member(
            update.message.chat.id, update.message.reply_to_message.from_user.id)

    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... No puedo expulsar administradores (⌒_⌒;)')
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.kick_chat_member(update.message.chat.id,
                             update.message.reply_to_message.forward_from.id)
        bot.unban_chat_member(update.message.chat.id,
                              update.message.reply_to_message.forward_from.id)
    else:
        bot.kick_chat_member(update.message.chat.id,
                             update.message.reply_to_message.from_user.id)
        bot.unban_chat_member(update.message.chat.id,
                              update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text('¡Expulsad@!')
    bot.send_sticker(update.message.chat.id, 'CAADAgADpxsAAuCjggf0_Fu4xLzgxAI')


def kick_me(bot, update):
    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... no tengo los permisos para expulsar usuarios (╥_╥)')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... No puedo expulsar administradores (⌒_⌒;)')
        return

    bot.kick_chat_member(update.message.chat.id, update.message.from_user.id)
    bot.unban_chat_member(update.message.chat.id, update.message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_text('¡Espero que vuelvas pronto! ( ; ω ; )')
    bot.send_sticker(update.message.chat.id, 'CAADAgADmhsAAuCjggeKLIclx5HvGQI')


def unban(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Uhm? No puedo desbanear a nadie si no respondes a un mensaje')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Lo siento, pero me dijeron que tú no puedes desbanear usuarios...')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... no tengo los permisos para desbanear usuarios (╥_╥)')
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.unban_chat_member(update.message.chat.id,
                              update.message.reply_to_message.forward_from.id)
    else:
        bot.unban_chat_member(update.message.chat.id,
                              update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text('¡Desbanead@! (o^▽^o)')
    bot.send_sticker(update.message.chat.id, 'CAADAgADshsAAuCjgge9W_YhLXZXrgI')
