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
	"os"
	"strconv"

	groupadminbot "gitlab.com/nahuelwexd/groupadmin-bot/internal/app/groupadmin-bot"
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

	bot := groupadminbot.BotNew(token)
	bot.Run(port)
}
