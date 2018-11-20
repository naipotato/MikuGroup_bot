# -*- coding: utf-8 -*-
#
# newmembers.py - This file is part of animux-bot
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


import os
from telegram import ChatAction, ParseMode

group_id = eval(os.environ['TELEGRAM_GROUP'])
print(type(group_id))


def added_to_group(bot, update):
    if update.message.chat.id != group_id:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id,
                         'Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)')
        bot.leave_chat(update.message.chat.id)
        return

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    bot.send_message(update.message.chat.id,
                     "Kon'nichiwa, Hatsune Miku desu! ＼(≧▽≦)／")
    bot.send_sticker(update.message.chat.id, 'CAADAgADsBsAAuCjggdzuy-p9Uzd2gI')
    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    bot.send_message(update.message.chat.id, 'Estoy aquí para ayudar a [Nahuel](tg://user?id=82982166) y a [Zoé]' +
                     '(tg://user?id=359710858) a administrar este increíble grupo, así que es un placer conocerlos ' +
                     '(◕‿◕)', ParseMode.MARKDOWN)


def filter_group(bot, update):
    if update.message.chat.id != group_id:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id, "Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)")
        bot.leave_chat(update.message.chat.id)


def new_chat_members(bot, update):
    if bot.get_me() in update.message.new_chat_members:
        added_to_group(bot, update)
        return

    if len(update.message.new_chat_members) == 1:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Hola {}, bienvenid@ al grupo!'.format(
            update.message.new_chat_members[0].first_name))
    else:
        update.message.reply_text('Hola, sean bienvenidos!')

    bot.send_sticker(update.message.chat.id, 'CAADAgADtBsAAuCjgge3gHY3V1-8zgI')
