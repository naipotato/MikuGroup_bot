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

}

func (bot *bot) run(port int) {

}

func (bot *bot) configureHandlers() {

}
