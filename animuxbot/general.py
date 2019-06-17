# -*- coding: utf-8 -*-
#
# general.py - This file is part of animux-bot
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


from telegram import ChatAction, ChatMember, ParseMode


def about(bot, update):
    acerca = '''<b>Hatsune Miku</b> @Animux_bot
<i>Versión: 0.6.0</i>

<i>Un excelente bot desarrollado para administrar el grupo @AnimuxOwO, además de tener muchos comandos divertidos :D</i>

<b>Desarrollado por:</b> <a href="tg://user?id=82982166">ηαнυεℓ ωεx∂</a>
<b>Código fuente:</b> https://github.com/nahuelwexd/AnimuxBot'''

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_text(acerca, ParseMode.HTML, True)


def help_message(bot, update):
    ayuda = '''Estos son los comandos que puedes usar conmigo ﾞ(˘ᵕ˘)

- `/ban` (por respuesta): banearé al usuario que respondiste, incluso si el mensaje fue reenviado.
- `/del` (por respuesta): borraré el mensaje al que respondiste.
- `/kick` (por respuesta): expulsaré al usuario, pero dejaré que pueda volver a entrar.
- `/kickme`: te expulsaré del grupo, pero podrás volver a entrar.
- `/pin` (por respuesta): anclaré el mensaje notificando a todos.
- `/pinmute` (por respuesta): anclaré el mensaje silencionsamente.
- `/unban` (por respuesta): le quitaré el ban al usuario al que respondiste, incluso si el mensaje es reenviado.'''

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_text(ayuda, ParseMode.MARKDOWN)


def love(bot, update):
    if update.message.from_user.id == 82982166 or update.message.from_user.id == 359710858:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('La pareja más hermosa que he conocido son [Zoé]' +
                                  '(tg://user?id=359710858) y [Nahuel](tg://user?id=82982166) ' +
                                  ':3\n\nEsos dos tortolitos enamorados se aman ' +
                                  'incondicionalmente, se acompañan en todo lo que pueden, ' +
                                  'y anteponen siempre las necesidades del otro ❤️',
                                  ParseMode.MARKDOWN)
        bot.send_sticker(update.message.chat.id,
                         'CAADAQADwQEAAuWyyh3shINoW9G1fwI')


def pin(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Emm... Qué mensaje debo anclar? (・・ ) ?')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_pin_messages and not chat_member.status == ChatMember.CREATOR:
        update.message.reply_sticker('CAADAgADoRsAAuCjggfsFEp1hLA7RQI')
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id,
                         'Tú no puedes anclar mensajes')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_pin_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'No tengo permisos para anclar mensajes (T_T)')
        return

    bot.pin_chat_message(update.message.chat.id,
                         update.message.reply_to_message.message_id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text('Anclado <(￣︶￣)>')


def pin_mute(bot, update):
    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Emm... Qué mensaje debo anclar? (・・ ) ?')
        return

    chat_member = bot.get_chat_member(
        update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_pin_messages and not chat_member.status == ChatMember.CREATOR:
        update.message.reply_sticker('CAADAgADoRsAAuCjggfsFEp1hLA7RQI')
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id,
                         'Tú no puedes anclar mensajes')
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_pin_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text(
            'No tengo permisos para anclar mensajes (T_T)')
        return

    bot.pin_chat_message(update.message.chat.id,
                         update.message.reply_to_message.message_id, True)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text('Anclado <(￣︶￣)>')


def di(bot, update, args):
    if args is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text('Emm... Qué es lo que debo decir? (・・ ) ?')
        return
    
    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_text(' '.join(args))

