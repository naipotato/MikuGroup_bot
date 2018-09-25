# -*- coding: utf-8 -*-
from telegram import ChatAction, ParseMode

from animuxbot.secrets import DEBUG_GROUP_ID, RELEASE_GROUP_ID


def added_to_group(bot, update):
    if bot.username == u'PruebasAnimux_bot':
        group_id = DEBUG_GROUP_ID
    elif bot.username == u'Animux_bot':
        group_id = RELEASE_GROUP_ID

    if update.message.chat.id != group_id:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id, "Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)")
        bot.leave_chat(update.message.chat.id)
        return

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    bot.send_message(update.message.chat.id, "Kon'nichiwa, Hatsune Miku desu! ＼(≧▽≦)／")
    bot.send_sticker(update.message.chat.id, "CAADAgADsBsAAuCjggdzuy-p9Uzd2gI")
    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    bot.send_message(update.message.chat.id, "Estoy aquí para ayudar a [Nahuel](tg://user?id=82982166) y a [Zoé]" +
                     "(tg://user?id=359710858) a administrar este increíble grupo, así que es un placer conocerlos " +
                     "(◕‿◕)", ParseMode.MARKDOWN)


def new_chat_members(bot, update):
    if bot.get_me() in update.message.new_chat_members:
        added_to_group(bot, update)
        return

    if len(update.message.new_chat_members) == 1:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Hola {}, bienvenid@ al grupo!".format(update.message.new_chat_members[0].first_name))
    else:
        update.message.reply_text("Hola, sean bienvenidos!")

    bot.send_sticker(update.message.chat.id, "CAADAgADtBsAAuCjgge3gHY3V1-8zgI")
