from ponyrevolution_bot import LOGGER, PORT, TOKEN, URL, WEBHOOK, updater


def main():
    if WEBHOOK:
        updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(URL + TOKEN)
    else:
        updater.start_polling()

    LOGGER.info('Bot @%s started.' % updater.bot.get_me().username)
    updater.idle()


if __name__ == '__main__':
    main()
