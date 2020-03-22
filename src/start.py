from telegram.ext import MessageHandler, RegexHandler, Filters

from teleg.telegram_events_handler import *
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def read_config_file():
    with open('config.json', 'r') as f:
        import json
        return json.load(f)


def configure_and_start_telegram_dispatcher(config_file):
    from telegram.ext import CommandHandler, Updater
    updater = Updater(token=config_file['token'], use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B11.get_value_escaped()), get_usd_actual))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B12.get_value_escaped()), get_usd_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B13.get_value_escaped()), get_usd_for_last_2_weeks))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B14.get_value_escaped()), get_usd_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B21.get_value_escaped()), get_eur_actual))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B22.get_value_escaped()), get_eur_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B23.get_value_escaped()), get_eur_for_last_2_weeks))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B24.get_value_escaped()), get_eur_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B31.get_value_escaped()), show_help))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B32.get_value_escaped()), show_link))

    dispatcher.add_handler(CommandHandler("test", test_output))
    logging.info('Starting updates polling')
    updater.start_polling()


if __name__ == '__main__':

    config = read_config_file()
    configure_and_start_telegram_dispatcher(config)
    logging.info("Started.")