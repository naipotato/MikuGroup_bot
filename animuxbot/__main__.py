# -*- coding: utf-8 -*-
import logging
import sys

from telegram import ChatAction
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

from animuxbot.ban import ban, kick, kick_me, unban
from animuxbot.deletemessages import delete
from animuxbot.general import pin, pin_mute, love, help_message, about
from animuxbot.newmembers import new_chat_members
from animuxbot.secrets import DEBUG_TOKEN, RELEASE_TOKEN, DEBUG_GROUP_ID, RELEASE_GROUP_ID

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def filter_group(bot, update):
    if bot.username == u'PruebasAnimux_bot':
        group_id = DEBUG_GROUP_ID
    elif bot.username == u'Animux_bot':
        group_id = RELEASE_GROUP_ID

    if update.message.chat.id != group_id:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id, "Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)")
        bot.leave_chat(update.message.chat.id)


def main():
    logger.info("Starting bot...")

    args = sys.argv[1:]

    if len(args) == 1 and args[0] == '--debug':
        logger.info("Configuration debug selected")
        updater = Updater(DEBUG_TOKEN)
    else:
        logger.info("Configuration release selected")
        updater = Updater(RELEASE_TOKEN)

    # Obtenemos el dispatcher para registrar los handlers
    dp = updater.dispatcher

    # Añadimos los distintos comandos
    dp.add_handler(CommandHandler("ban", ban, Filters.group))
    dp.add_handler(CommandHandler("del", delete, Filters.group))
    dp.add_handler(CommandHandler("kick", kick, Filters.group))
    dp.add_handler(CommandHandler("kickme", kick_me, Filters.group))
    dp.add_handler(CommandHandler("pin", pin, Filters.group))
    dp.add_handler(CommandHandler("pinmute", pin_mute, Filters.group))
    dp.add_handler(CommandHandler("unban", unban, Filters.group))
    dp.add_handler(CommandHandler("love", love, Filters.group))
    dp.add_handler(CommandHandler("help", help_message, Filters.group))
    dp.add_handler(CommandHandler("about", about, Filters.group))

    # Añadimos los handlers para mensajes
    dp.add_handler(MessageHandler(Filters.group & Filters.status_update.new_chat_members, new_chat_members))
    dp.add_handler(MessageHandler(Filters.group, filter_group))

    # Hacemos un log de los errores
    dp.add_error_handler(error)

    logger.info("Handlers added succesfully")

    # Iniciamos el bot
    updater.start_polling()

    logger.info("Bot started")

    # Llamamos a la función idle para que no se cierre automáticamente
    updater.idle()


if __name__ == '__main__':
    main()
