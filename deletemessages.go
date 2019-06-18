package main

import (
	"log"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func delete(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage != nil {
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
