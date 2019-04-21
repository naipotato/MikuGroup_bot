# Copyright (C) 2019 Nahuel Gomez Castro <nahual_gomca@outlook.com.ar>
#
# This file is part of Animux bot.
#
# Animux bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Animux bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List, Optional

from telegram import Message


def extract_user_and_text(message: Message, args: List[str]) -> (Optional[int], Optional[str]):
    replied_message = message.reply_to_message

    if replied_message:
        user_id = replied_message.from_user.id
        reason = message.text.split(None, 1)

        if len(reason) < 2:
            return user_id, None

        return user_id, reason[1]
    else:
        return None, None
