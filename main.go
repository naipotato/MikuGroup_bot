package main

import (
	"log"
	"os"
	"strconv"
)

func main() {
	token := os.Getenv("TELEGRAM_TOKEN")
	if token == "" {
		log.Fatal("Token is empty")
	}

	port, err := strconv.Atoi(os.Getenv("PORT"))
	if err != nil {
		log.Fatal(err)
	}

	bot := botNew(token)
	bot.run(port)
}
