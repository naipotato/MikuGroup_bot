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

import argparse
import logging
import os

from telegram.ext import Updater

# Enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s\t%(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.info('Logging enabled.')

# Enable arg parser
parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug', help='enable debug mode', action='store_true')
ARGS = parser.parse_args()
LOGGER.info('Arg parser enabled')

# Load configs
ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', '')
    PORT = int(os.environ.get('PORT', 8443))
else:
    if ARGS.debug:
        from animux_bot.config import Debug as Config
    else:
        from animux_bot.config import Release as Config

    TOKEN = Config.TOKEN
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT

LOGGER.info('Configs loaded')

LOGGER.info('Starting bot...')
UPDATER = Updater(token=TOKEN)
DISPATCHER = UPDATER.dispatcher
