# -*- coding: utf-8 -*-
# 
# deletemessages.py - This file is part of animux-bot
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


def delete(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Emm... No respondiste al mensaje que debo borrar.')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_delete_messages and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Lo siento, pero no estás autorizad@ para borrar mensajes.')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_delete_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'Etto... no tengo los permisos para borrar mensajes (╥_╥)')
        return

    bot.delete_message(update.message.chat.id,
                       update.message.reply_to_message.message_id)
    bot.delete_message(update.message.chat.id, update.message.message_id)
