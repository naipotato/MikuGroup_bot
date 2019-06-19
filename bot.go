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
	"net/http"
	"strconv"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

type bot struct {
	token   string
	botAPI  *tgbotapi.BotAPI
	updates tgbotapi.UpdatesChannel
}

func botNew(token string) *bot {
	bot := new(bot)

	bot.token = token

	botAPI, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Created new BotAPI")

	bot.botAPI = botAPI

	return bot
}

func (bot *bot) run(port int) {
	_, err := bot.botAPI.SetWebhook(tgbotapi.NewWebhook("https://groupadmin-bot.herokuapp.com/" + bot.token))
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Webhook enabled")

	info, err := bot.botAPI.GetWebhookInfo()
	if err != nil {
		log.Fatal(err)
	} else if info.LastErrorDate != 0 {
		log.Printf("Telegram callback failed: %s", info.LastErrorMessage)
	}

	bot.botAPI.Debug = true

	bot.updates = bot.botAPI.ListenForWebhook("/" + bot.token)
	go http.ListenAndServe("0.0.0.0:"+strconv.Itoa(port), nil)

	bot.listenToCommands()
}

func (bot *bot) listenToCommands() {
	for update := range bot.updates {
		log.Println("Update received!")

		if update.Message == nil {
			continue
		}

		if update.Message.Chat.Type == "supergroup" {
			if update.Message.IsCommand() {
				switch update.Message.Command() {
				case "ban":
					log.Println("Ban command received")
					ban(bot.botAPI, update)
					break
				case "del":
					log.Println("Del command received")
					delete(bot.botAPI, update)
					break
				case "kick":
					log.Println("Kick command received")
					kick(bot.botAPI, update)
					break
				case "kickme":
					log.Println("KickMe command received")
					kickMe(bot.botAPI, update)
					break
				case "pin":
					log.Println("Pin command received")
					pin(bot.botAPI, update)
					break
				case "pinmute":
					log.Println("PinMute command received")
					pinMute(bot.botAPI, update)
					break
				case "unban":
					log.Println("Unban command received")
					unban(bot.botAPI, update)
					break
				case "love":
					log.Println("Love command received")
					love(bot.botAPI, update)
					break
				case "help":
					log.Println("Help command received")
					helpMessage(bot.botAPI, update)
					break
				case "about":
					log.Println("About command received")
					about(bot.botAPI, update)
					break
				case "di":
					log.Println("Di command received")
					di(bot.botAPI, update)
					break
				}
			}

			filterGroup(bot.botAPI, update)

			if update.Message.NewChatMembers != nil {
				newChatMembers(bot.botAPI, update)
			}
		}
	}
}
