// GroupAdmin Bot
// Copyright (C) 2018 - 2019 Nahuel Gomez Castro <nahual_gomca@outlook.com.ar>
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

package main

import (
	"log"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func about(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	acerca := `<b>Hatsune Miku</b> @PonyRevolution_bot
<i>Versión: 1.0.0</i>

<i>Un excelente bot desarrollado para administrar el grupo @AnimuxOwO, además de tener muchos comandos divertidos :D</i>

<b>Desarrollado por:</b> <a href="tg://user?id=82982166">ηαнυεℓ ωεx∂</a>
<b>Código fuente:</b> https://gitlab.com/nahuelwexd/groupadmin-bot`

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, acerca)
	msg.ParseMode = "HTML"
	msg.ReplyToMessageID = update.Message.MessageID
	msg.DisableWebPagePreview = true
	bot.Send(msg)
}

func helpMessage(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	ayuda := `Estos son los comandos que puedes usar conmigo ﾞ(˘ᵕ˘)

- <code>/ban</code> (por respuesta): banearé al usuario que respondiste, incluso si el mensaje fue reenviado.
- <code>/del</code> (por respuesta): borraré el mensaje al que respondiste.
- <code>/kick</code> (por respuesta): expulsaré al usuario, pero dejaré que pueda volver a entrar.
- <code>/kickme</code>: te expulsaré del grupo, pero podrás volver a entrar.
- <code>/pin</code> (por respuesta): anclaré el mensaje notificando a todos.
- <code>/pinmute</code> (por respuesta): anclaré el mensaje silencionsamente.
- <code>/unban</code> (por respuesta): le quitaré el ban al usuario al que respondiste, incluso si el mensaje es reenviado.
- <code>/di</code>: repetiré lo que has dicho.`

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, ayuda)
	msg.ParseMode = "HTML"
	msg.ReplyToMessageID = update.Message.MessageID
	bot.Send(msg)
}

func love(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.From.ID == 82982166 || update.Message.From.ID == 359710858 {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "La pareja más hermosa que he conocido son [Zoé]"+
			"(tg://user?id=359710858) y [Nahuel](tg://user?id=82982166) :3\n\nEsos dos tortolitos enamorados se aman "+
			"inconcicionalmente, se acompañan en todo lo que pueden, y anteponen siempre las necesidades del otro ❤️")
		msg.ParseMode = "Markdown"
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAQADwQEAAuWyyh3shINoW9G1fwI"))
	}
}

func pin(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage == nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Emm... Qué mensaje debo anclar? (・・ ) ?")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	chatMember, err := bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: update.Message.From.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if !chatMember.CanPinMessages && chatMember.Status != "creator" {
		sticker := tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADoRsAAuCjggfsFEp1hLA7RQI")
		sticker.ReplyToMessageID = update.Message.MessageID
		bot.Send(sticker)
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		bot.Send(tgbotapi.NewMessage(update.Message.Chat.ID, "Tú no puedes anclar mensajes"))
		return
	}

	chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: bot.Self.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if !chatMember.CanPinMessages {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "No tengo permisos para anclar mensajes (T_T)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	bot.PinChatMessage(tgbotapi.PinChatMessageConfig{
		ChatID:    update.Message.Chat.ID,
		MessageID: update.Message.ReplyToMessage.MessageID,
	})

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Anclado <(￣︶￣)>")
	msg.ReplyToMessageID = update.Message.ReplyToMessage.MessageID
}

func pinMute(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage == nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Emm... Qué mensaje debo anclar? (・・ ) ?")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	chatMember, err := bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: update.Message.From.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if !chatMember.CanPinMessages && chatMember.Status != "creator" {
		sticker := tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADoRsAAuCjggfsFEp1hLA7RQI")
		sticker.ReplyToMessageID = update.Message.MessageID
		bot.Send(sticker)
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		bot.Send(tgbotapi.NewMessage(update.Message.Chat.ID, "Tú no puedes anclar mensajes"))
		return
	}

	chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: bot.Self.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if !chatMember.CanPinMessages {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "No tengo permisos para anclar mensajes (T_T)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	bot.PinChatMessage(tgbotapi.PinChatMessageConfig{
		ChatID:              update.Message.Chat.ID,
		MessageID:           update.Message.ReplyToMessage.MessageID,
		DisableNotification: true,
	})

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Anclado <(￣︶￣)>")
	msg.ReplyToMessageID = update.Message.ReplyToMessage.MessageID
}

func di(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.CommandArguments() == "" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Emm... Qué es lo que debo decir? (・・ ) ?")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))

	msg := tgbotapi.NewMessage(update.Message.Chat.ID, update.Message.CommandArguments())
	msg.ReplyToMessageID = update.Message.MessageID
	msg.ParseMode = "Markdown"
	bot.Send(msg)
}
