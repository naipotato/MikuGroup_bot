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

package groupadminbot

import (
	"log"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func delete(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage == nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Emm... No respondiste al mensaje que debo borrar")
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

	if !chatMember.CanDeleteMessages && chatMember.Status != "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Lo siento, pero no estás autorizad@ para borrar mensajes.")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
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

	if !chatMember.CanDeleteMessages {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... no tengo los permisos para borrar mensajes (╥_╥)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	bot.DeleteMessage(tgbotapi.DeleteMessageConfig{
		ChatID:    update.Message.Chat.ID,
		MessageID: update.Message.ReplyToMessage.MessageID,
	})
	bot.DeleteMessage(tgbotapi.DeleteMessageConfig{
		ChatID:    update.Message.Chat.ID,
		MessageID: update.Message.MessageID,
	})
}
