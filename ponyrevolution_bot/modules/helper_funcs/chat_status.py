# -*- coding: utf-8 -*-
from functools import wraps

from telegram import Bot, ChatAction, ChatMember, Update


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
