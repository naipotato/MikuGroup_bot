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

import importlib

from . import LOGGER, PORT, TOKEN, UPDATER, URL, WEBHOOK
from .modules import ALL_MODULES

# Imported modules
IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module(
        'animux_bot.modules.' + module_name)
    IMPORTED[imported_module.__mod_name__.lower()] = imported_module


def main():
    if WEBHOOK:
        UPDATER.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
        UPDATER.bot.set_webhook(URL + TOKEN)
    else:
        UPDATER.start_polling()

    LOGGER.info('Bot @%s started.' % UPDATER.bot.get_me().username)
    UPDATER.idle()


if __name__ == '__main__':
    LOGGER.info('Successfully loaded modules: %s' % str(ALL_MODULES))
    main()
