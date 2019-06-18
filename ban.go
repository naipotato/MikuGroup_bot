package main

import (
	"log"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func ban(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage == nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Uhm? No puedo banear a nadie si no respondes a un mensaje")
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

	if !chatMember.CanRestrictMembers && chatMember.Status != "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID,
			"Lo siento, pero me dijeron que tú no puedes banear usuarios...")
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

	if !chatMember.CanRestrictMembers {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... no tengo los permisos para banear usuarios (╥_╥)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	var user *tgbotapi.User
	if update.Message.ReplyToMessage.ForwardFrom != nil {
		user = update.Message.ReplyToMessage.ForwardFrom
	} else {
		user = update.Message.ReplyToMessage.From
	}

	if user.ID == bot.Self.ID {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Hey! Esa soy yo! (O.O)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADrRsAAuCjgge1g6be76IiHgI"))
	}

	if update.Message.ReplyToMessage.ForwardFrom != nil {
		chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.ForwardFrom.ID,
		})
		if err != nil {
			log.Println(err)
			return
		}
	} else {
		chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.From.ID,
		})
		if err != nil {
			log.Println(err)
			return
		}
	}

	if chatMember.Status == "administrator" || chatMember.Status == "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... No puedo banear administradores (⌒_⌒;)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	if update.Message.ReplyToMessage.ForwardFrom != nil {
		bot.KickChatMember(tgbotapi.KickChatMemberConfig{
			ChatMemberConfig: tgbotapi.ChatMemberConfig{
				ChatID: update.Message.Chat.ID,
				UserID: update.Message.ForwardFrom.ID,
			},
		})
	} else {
		bot.KickChatMember(tgbotapi.KickChatMemberConfig{
			ChatMemberConfig: tgbotapi.ChatMemberConfig{
				ChatID: update.Message.Chat.ID,
				UserID: update.Message.ReplyToMessage.From.ID,
			},
		})
	}

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "¡Banead@!")
	msg.ReplyToMessageID = update.Message.MessageID
	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADpxsAAuCjggf0_Fu4xLzgxAI"))
}

func kick(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage == nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID,
			"Uhm? No puedo expulsar a nadie si no respondes a un mensaje")
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

	if !chatMember.CanRestrictMembers && chatMember.Status != "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID,
			"Lo siento, pero me dijeron que tú no puedes expulsar usuarios...")
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

	if !chatMember.CanRestrictMembers {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... no tengo los permisos para expulsar usuarios (╥_╥)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	var user *tgbotapi.User
	if update.Message.ReplyToMessage.ForwardFrom != nil {
		user = update.Message.ReplyToMessage.ForwardFrom
	} else {
		user = update.Message.ReplyToMessage.From
	}

	if user.ID == bot.Self.ID {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Hey! Esa soy yo! (O.O)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADrRsAAuCjgge1g6be76IiHgI"))
		return
	}

	if update.Message.ReplyToMessage.ForwardFrom != nil {
		chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.ForwardFrom.ID,
		})
		if err != nil {
			log.Println(err)
			return
		}
	} else {
		chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.From.ID,
		})
		if err != nil {
			log.Println(err)
			return
		}
	}

	if chatMember.Status == "administrator" || chatMember.Status == "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... No puedo expulsar administradores (⌒_⌒;)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	if update.Message.ReplyToMessage.ForwardFrom != nil {
		bot.KickChatMember(tgbotapi.KickChatMemberConfig{
			ChatMemberConfig: tgbotapi.ChatMemberConfig{
				ChatID: update.Message.Chat.ID,
				UserID: update.Message.ReplyToMessage.ForwardFrom.ID,
			},
		})
		bot.UnbanChatMember(tgbotapi.ChatMemberConfig{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.ForwardFrom.ID,
		})
	} else {
		bot.KickChatMember(tgbotapi.KickChatMemberConfig{
			ChatMemberConfig: tgbotapi.ChatMemberConfig{
				ChatID: update.Message.Chat.ID,
				UserID: update.Message.ReplyToMessage.From.ID,
			},
		})
		bot.UnbanChatMember(tgbotapi.ChatMemberConfig{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.From.ID,
		})
	}

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "¡Expulsad@!")
	msg.ReplyToMessageID = update.Message.ReplyToMessage.MessageID
	bot.Send(msg)
	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADpxsAAuCjggf0_Fu4xLzgxAI"))
}

func kickMe(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	chatMember, err := bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: bot.Self.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if !chatMember.CanRestrictMembers {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... no tengo los permisos para expulsar usuario (╥_╥)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	chatMember, err = bot.GetChatMember(tgbotapi.ChatConfigWithUser{
		ChatID: update.Message.Chat.ID,
		UserID: update.Message.From.ID,
	})
	if err != nil {
		log.Println(err)
		return
	}

	if chatMember.Status == "administrator" || chatMember.Status == "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Etto... No puedo expulsar administradores (⌒_⌒;)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	bot.KickChatMember(tgbotapi.KickChatMemberConfig{
		ChatMemberConfig: tgbotapi.ChatMemberConfig{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.From.ID,
		},
	})
	bot.UnbanChatMember(tgbotapi.ChatMemberConfig{
		ChatID: update.Message.Chat.ID,
		UserID: update.Message.From.ID,
	})

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "¡Espero que vuelvas pronto! ( ; ω ; )")
	msg.ReplyToMessageID = update.Message.MessageID
	bot.Send(msg)
	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADmhsAAuCjggeKLIclx5HvGQI"))
}

func unban(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if update.Message.ReplyToMessage != nil {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Uhm? No puedo banear a nadie si no respondes a un mensaje")
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

	if !chatMember.CanRestrictMembers && chatMember.Status != "creator" {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID,
			"Lo siento, pero me dijeron que tú no puedes desbanear usuarios...")
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

	if !chatMember.CanRestrictMembers {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID,
			"Etto... no tengo los permisos para desbanear usuarios (╥_╥)")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
		return
	}

	if update.Message.ReplyToMessage.ForwardFrom != nil {
		bot.UnbanChatMember(tgbotapi.ChatMemberConfig{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.ForwardFrom.ID,
		})
	} else {
		bot.UnbanChatMember(tgbotapi.ChatMemberConfig{
			ChatID: update.Message.Chat.ID,
			UserID: update.Message.ReplyToMessage.From.ID,
		})
	}

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "¡Desbanead@! (o^▽^o)")
	msg.ReplyToMessageID = update.Message.ReplyToMessage.MessageID
	bot.Send(msg)
	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADshsAAuCjgge9W_YhLXZXrgI"))
}
