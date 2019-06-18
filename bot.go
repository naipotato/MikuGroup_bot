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

	bot.botAPI = botAPI

	return bot
}

func (bot *bot) run(port int) {
	_, err := bot.botAPI.SetWebhook(tgbotapi.NewWebhook("https://ponyrevolution-bot.herokuapp.com/" + bot.token))
	if err != nil {
		log.Fatal(err)
	}

	info, err := bot.botAPI.GetWebhookInfo()
	if err != nil {
		log.Fatal(err)
	} else if info.LastErrorDate != 0 {
		log.Printf("Telegram callback failed: %s", info.LastErrorMessage)
	}

	bot.updates = bot.botAPI.ListenForWebhook("/" + bot.token)
	go http.ListenAndServe("0.0.0.0:"+strconv.Itoa(port), nil)

	bot.listenToCommands()
}

func (bot *bot) listenToCommands() {
	for update := range bot.updates {
		if update.Message != nil {
			continue
		}

		if update.Message.Chat.Type == "supergroup" {
			if update.Message.IsCommand() {
				switch update.Message.Command() {
				case "ban":
					ban(bot.botAPI, update)
					break
				case "del":
					delete(bot.botAPI, update)
					break
				case "kick":
					kick(bot.botAPI, update)
					break
				case "kickme":
					kickMe(bot.botAPI, update)
					break
				case "pin":
					pin(bot.botAPI, update)
					break
				case "pinmute":
					pinMute(bot.botAPI, update)
					break
				case "unban":
					unban(bot.botAPI, update)
					break
				case "love":
					love(bot.botAPI, update)
					break
				case "help":
					helpMessage(bot.botAPI, update)
					break
				case "about":
					about(bot.botAPI, update)
					break
				case "di":
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
