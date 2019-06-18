package main

import tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"

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
