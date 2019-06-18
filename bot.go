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

}

func (bot *bot) configureHandlers() {

}
