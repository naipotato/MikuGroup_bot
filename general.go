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
