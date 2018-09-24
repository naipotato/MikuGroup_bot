# -*- coding: utf-8 -*-
import logging

from telegram import ChatAction, ChatMember

logger = logging.getLogger()


def ban(bot, update):
    logger.info("Command /ban received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Uhm? No puedo banear a nadie si no respondes a un mensaje")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Lo siento, pero me dijeron que tú no puedes banear usuarios...")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... no tengo los permisos para banear usuarios (╥_╥)")
        return

    if update.message.reply_to_message.forward_from is not None:
        user = update.message.reply_to_message.forward_from
    else:
        user = update.message.reply_to_message.from_user

    if user == bot.get_me():
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Hey! Esa soy yo! (O.O)")
        bot.send_sticker(update.message.chat.id, "CAADAgADrRsAAuCjgge1g6be76IiHgI")
        return

    if update.message.reply_to_message.forward_from is not None:
        chat_member = bot.get_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        chat_member = bot.get_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)

    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... No puedo banear administradores (⌒_⌒;)")
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text("¡Banead@!")
    bot.send_sticker(update.message.chat.id, "CAADAgADpxsAAuCjggf0_Fu4xLzgxAI")


def kick(bot, update):
    logger.info("Command /kick received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Uhm? No puedo expulsar a nadie si no respondes a un mensaje")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Lo siento, pero me dijeron que tú no puedes expulsar usuarios...")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... no tengo los permisos para expulsar usuarios (╥_╥)")
        return

    if update.message.reply_to_message.forward_from is not None:
        user = update.message.reply_to_message.forward_from
    else:
        user = update.message.reply_to_message.from_user

    if user == bot.get_me():
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Hey! Esa soy yo! (O.O)")
        bot.send_sticker(update.message.chat.id, "CAADAgADrRsAAuCjgge1g6be76IiHgI")
        return

    if update.message.reply_to_message.forward_from is not None:
        chat_member = bot.get_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        chat_member = bot.get_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)

    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... No puedo expulsar administradores (⌒_⌒;)")
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
        bot.unban_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)
        bot.unban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text("¡Expulsad@!")
    bot.send_sticker(update.message.chat.id, "CAADAgADpxsAAuCjggf0_Fu4xLzgxAI")


def kick_me(bot, update):
    logger.info("Command /kickme received")

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... no tengo los permisos para expulsar usuarios (╥_╥)")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if chat_member.status == ChatMember.ADMINISTRATOR or chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... No puedo expulsar administradores (⌒_⌒;)")
        return

    bot.kick_chat_member(update.message.chat.id, update.message.from_user.id)
    bot.unban_chat_member(update.message.chat.id, update.message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_text("¡Espero que vuelvas pronto! ( ; ω ; )")
    bot.send_sticker(update.message.chat.id, "CAADAgADmhsAAuCjggeKLIclx5HvGQI")


def unban(bot, update):
    logger.info("Command /unban received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Uhm? No puedo desbanear a nadie si no respondes a un mensaje")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_restrict_members and not chat_member.status == ChatMember.CREATOR:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Lo siento, pero me dijeron que tú no puedes desbanear usuarios...")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_restrict_members:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Etto... no tengo los permisos para desbanear usuarios (╥_╥)")
        return

    if update.message.reply_to_message.forward_from is not None:
        bot.unban_chat_member(update.message.chat.id, update.message.reply_to_message.forward_from.id)
    else:
        bot.unban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text("¡Desbanead@! (o^▽^o)")
    bot.send_sticker(update.message.chat.id, "CAADAgADshsAAuCjgge9W_YhLXZXrgI")
