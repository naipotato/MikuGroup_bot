import importlib

from pony_bot import LOGGER, PORT, TOKEN, URL, WEBHOOK, updater
from pony_bot.modules import ALL_MODULES

# Import modules
IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module('pony_bot.modules.' + module_name)
    IMPORTED[imported_module.__mod_name__.lower()] = imported_module


def main():
    if WEBHOOK:
        updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(URL + TOKEN)
    else:
        updater.start_polling()

    LOGGER.info('Bot @%s started.' % updater.bot.get_me().username)
    updater.idle()


if __name__ == '__main__':
    LOGGER.info('Successfully loaded modules: %s' % str(ALL_MODULES))
    main()
