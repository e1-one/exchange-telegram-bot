from telegram.ext import MessageHandler, RegexHandler, Filters

from teleg.bot_constants import BotButton
from value_analyzer import ChangeAnalyzer
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def read_config_file():
    with open('config.json', 'r') as f:
        import json
        return json.load(f)


def configure_and_start_telegram_dispatcher(config_file, analyzer):
    from telegram.ext import CommandHandler, Updater
    from teleg.telegram_events_handler import EventHandler
    eh = EventHandler(analyzer)
    updater = Updater(token=config_file['token'], use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B11.get_value_escaped()), eh.get_usd))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B12.get_value_escaped()), eh.get_usd_for_last5_days))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B13.get_value_escaped()), eh.get_usd_for_last_2_weeks))
    dispatcher.add_handler(CommandHandler('start', eh.start))
    dispatcher.add_handler(CommandHandler('b', eh.get_usd_for_last5_days))
    dispatcher.add_handler(CommandHandler('c', eh.get_usd_for_last_2_weeks))
    logging.info('Starting updates polling')
    updater.start_polling()


if __name__ == '__main__':
    anal = ChangeAnalyzer()

    config = read_config_file()
    configure_and_start_telegram_dispatcher(config, anal)
    anal.analyze_avg_task()
    logging.info("Started.")