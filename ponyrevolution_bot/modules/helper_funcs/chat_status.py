# -*- coding: utf-8 -*-
from functools import wraps

from telegram import Bot, Update


def bot_can_restrict(func):
    @wraps(func)
    def restrict_rights(bot: Bot, update: Update, *args, **kwargs):
        if update.effective_chat.get_member(bot.id).can_restrict_members:
            return func(bot, update, *args, **kwargs)
        else:
            update.effective_message.reply_text(
                'Etto... no tengo los permisos para banear usuarios (╥_╥)')
    
    return restrict_rights
