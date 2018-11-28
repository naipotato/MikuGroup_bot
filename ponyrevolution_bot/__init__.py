import logging
import argparse
import os

from telegram.ext import Updater


# Enable logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.info('Logger enabled.')


# Enable args
parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug', help='enable debug mode', action='store_true')
ARGS = parser.parse_args()
LOGGER.info('Args enabled')


# Load configs
ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', '')
    PORT = int(os.environ.get('PORT', 8443))
else:
    if ARGS.debug:
        from ponyrevolution_bot.config import Debug as Config
    else:
        from ponyrevolution_bot.config import Release as Config
    
    TOKEN = Config.TOKEN
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT

LOGGER.info('Configs loaded.')


LOGGER.info('Starting bot...')
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
