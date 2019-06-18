package main

import (
	"fmt"
	"log"
	"os"
	"strconv"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func addedToGroup(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	groupID, err := strconv.Atoi(os.Getenv("TELEGRAM_GROUP"))
	if err != nil {
		log.Println(err)
		return
	}

	if update.Message.Chat.ID != int64(groupID) {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		bot.Send(tgbotapi.NewMessage(update.Message.Chat.ID, "Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)"))
		bot.LeaveChat(tgbotapi.ChatConfig{
			ChatID: update.Message.Chat.ID,
		})
		return
	}

	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	bot.Send(tgbotapi.NewMessage(update.Message.Chat.ID, "Kon'nichiwa, Hatsune Miku desu! ＼(≧▽≦)／"))
	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADsBsAAuCjggdzuy-p9Uzd2gI"))
	bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Estoy aquí para ayudar a [Nahuel](tg://user?id=82982166) y a "+
		"[Zoé](tg://user?id=359710858) a administrar este increíble grupo, así que es un placer conocerlos (◕‿◕)")
	msg.ParseMode = "Markdown"
	bot.Send(msg)
}

func filterGroup(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	groupID, err := strconv.Atoi(os.Getenv("TELEGRAM_GROUP"))
	if err != nil {
		log.Println(err)
		return
	}

	if update.Message.Chat.ID != int64(groupID) {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		bot.Send(tgbotapi.NewMessage(update.Message.Chat.ID, "Eh? Qué hago aquí? Esto no es @AnimuxOwO! (>_<)"))
		bot.LeaveChat(tgbotapi.ChatConfig{
			ChatID: update.Message.Chat.ID,
		})
	}
}

func contains(a *[]tgbotapi.User, x tgbotapi.User) bool {
	for _, n := range *a {
		if x == n {
			return true
		}
	}

	return false
}

func newChatMembers(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
	if contains(update.Message.NewChatMembers, bot.Self) {
		addedToGroup(bot, update)
		return
	}

	if len(*update.Message.NewChatMembers) == 1 {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, fmt.Sprintf("Hola %s, bienvenid@ al grupo!",
			(*update.Message.NewChatMembers)[0].FirstName))
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
	} else {
		bot.Send(tgbotapi.NewChatAction(update.Message.Chat.ID, tgbotapi.ChatTyping))
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Hola, sean bienvenid@s!")
		msg.ReplyToMessageID = update.Message.MessageID
		bot.Send(msg)
	}

	bot.Send(tgbotapi.NewStickerShare(update.Message.Chat.ID, "CAADAgADtBsAAuCjgge3gHY3V1-8zgI"))
}
