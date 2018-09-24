# -*- coding: utf-8 -*-
import logging

from telegram import ChatAction, ChatMember

logger = logging.getLogger()


def delete(bot, update):
    logger.info("Command /del received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Emm... No respondiste al mensaje que debo borrar.")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_delete_messages and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Lo siento, pero no estás autorizad@ para borrar mensajes.")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_delete_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... no tengo los permisos para borrar mensajes (╥_╥)")
        return

    bot.delete_message(update.message.chat.id, update.message.reply_to_message.message_id)
    bot.delete_message(update.message.chat.id, update.message.message_id)
