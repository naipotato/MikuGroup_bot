# -*- coding: utf-8 -*-
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

from functools import wraps

from telegram import Bot, Chat, ChatAction, ChatMember, Update


def bot_can_restrict(func):
    @wraps(func)
    def restrict_rights(bot: Bot, update: Update, *args, **kwargs):
        chat_member = update.effective_chat.get_member(bot.id)

        if chat_member.can_restrict_members:
            return func(bot, update, *args, **kwargs)
        else:
            bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
            update.effective_message.reply_text(
                'Etto... no tengo los permisos para banear usuarios (╥_╥)')

    return restrict_rights


def user_can_restrict(func):
    @wraps(func)
    def restrict_rights(bot: Bot, update: Update, *args, **kwargs):
        chat_member = update.effective_chat.get_member(
            update.effective_user.id)

        if chat_member.can_restrict_members or chat_member.status == ChatMember.CREATOR:
            return func(bot, update, *args, **kwargs)
        else:
            bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
            update.effective_message.reply_text(
                'Lo siento, pero me dijeron que tú no puedes banear usuarios...')

    return restrict_rights


def is_user_ban_protected(chat: Chat, user_id: int, member: ChatMember = None) -> bool:
    if chat.type == Chat.PRIVATE or chat.all_members_are_administrators:
        return True

    if not member:
        member = chat.get_member(user_id)

    return member.status in (ChatMember.ADMINISTRATOR, ChatMember.CREATOR)
