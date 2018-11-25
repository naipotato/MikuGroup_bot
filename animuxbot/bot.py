# bot.py - This file is part of animux-bot
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


from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

from animuxbot.ban import ban, kick, kick_me, unban
from animuxbot.deletemessages import delete
from animuxbot.general import pin, pin_mute, love, help_message, about, admin_list
from animuxbot.newmembers import new_chat_members, filter_group


class Bot(object):

    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(token)

        self.configure_handlers(self.updater.dispatcher)

    def run(self, port: int):
        self.updater.start_webhook(listen='0.0.0.0', port=port, url_path=self.token)
        self.updater.bot.set_webhook('https://animux-bot.herokuapp.com/' + self.token)
        self.updater.idle()
    
    def configure_handlers(self, dispatcher):
        dispatcher.add_handler(CommandHandler('adminlist', admin_list, Filters.group))
        dispatcher.add_handler(CommandHandler('ban', ban, Filters.group))
        dispatcher.add_handler(CommandHandler('del', delete, Filters.group))
        dispatcher.add_handler(CommandHandler('kick', kick, Filters.group))
        dispatcher.add_handler(CommandHandler('kickme', kick_me, Filters.group))
        dispatcher.add_handler(CommandHandler('pin', pin, Filters.group))
        dispatcher.add_handler(CommandHandler('pinmute', pin_mute, Filters.group))
        dispatcher.add_handler(CommandHandler('unban', unban, Filters.group))
        dispatcher.add_handler(CommandHandler('love', love, Filters.group))
        dispatcher.add_handler(CommandHandler('help', help_message, Filters.group))
        dispatcher.add_handler(CommandHandler('about', about, Filters.group))

        dispatcher.add_handler(MessageHandler(Filters.group & Filters.status_update.new_chat_members, new_chat_members))
        dispatcher.add_handler(MessageHandler(Filters.group, filter_group))
