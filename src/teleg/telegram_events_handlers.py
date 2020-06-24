import logging
from datetime import timedelta, date

from telegram import ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from helper.formatted_output import get_html_table_formatted, get_html_table_formatted_nbu
from helper.tables_finance_page_parser import get_actual_data, get_data_for_date_from_cache
from model.currency_type import CurrencyType
from model.page_data_object import PageDataObject
from model.source_type import SourceType
from teleg.bot_constants import BotButton

index_message = '''
Курс валют в обмінниках України 🇺🇦

Як користуватися ботом?: 
Просто натисніть на кнопку телеграм-клавіатури, щоб отримати інфррмацію, а саме: середнє значення курсу \
купівлі/продажу валюти в обмінниках або банках України за вибраний період.

/help - ❓ допомога 
/more - ℹ більше інформації 
'''

help_message = '''
Позначення:
┣ 🏪 - символ обмінника
┣ 🏦 - символ банку
┣ купів. - середній курс купівлі валюти
┣ продаж - середній курс продажі валюти
┣ НБУ - Курс валют по Національному Банку України
┗  √- колонка відображення коливань курсу, де:
  ┣   '▏ ' - мінімум для заданого періоду
  ┗   '▉' - максимум для періоду
'''

link = '''
[Сайт НБУ](https://bank.gov.ua/markets) національного банку україн - тут багато інфографіків,\
 новин та актуальний курс валют по НБУ.
[Finance.ua](https://tables.finance.ua/ua/currency/cash/-/ua,0,7oiylpmiow8iy1smadi/usd/2#3:0)\
 - курс валют в обмінниках, новини, форум.
'''

custom_keyboard = [
    [BotButton.B12.value, BotButton.B14.value],
    [BotButton.B22.value, BotButton.B24.value],

    [BotButton.B32.value, BotButton.B34.value],
    [BotButton.B42.value, BotButton.B44.value],

    [BotButton.B51.value],

    [BotButton.B91.value, BotButton.B92.value],
]
reply_keyboard_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=False, selective=True)


def start(update, context):
    logging.info(
        f"Showing /start output to {update.message.chat_id} chat. Name: {update.message.chat.first_name} \
        LastName: {update.message.chat.last_name}")
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=index_message,
                             reply_markup=reply_keyboard_markup)


def default(update, context):
    logging.info(f"Unexpected user text input.  Update.message: {update.message}")
    start(update, context)



def error(update, context):
    logging.info(
        f" Error happened. Update: {update}")
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN,
                             text="Server error. Please notify bot owner.",
                             reply_markup=reply_keyboard_markup)


def show_help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=help_message,
                             reply_markup=reply_keyboard_markup)


def show_link(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=link,
                             reply_markup=reply_keyboard_markup)


def get_usd_exch_actual(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.USD, 0)


def get_usd_exch_for_last_week(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.USD, 7)


def get_usd_exch_for_last_month(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.USD, 30)


def get_eur_exch_actual(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.Euro, 0)


def get_eur_exch_for_last_week(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.Euro, 7)


def get_eur_exch_for_last_month(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.EXCHANGER, CurrencyType.Euro, 30)


def get_usd_bank_actual(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.USD, 0)


def get_usd_bank_for_last_week(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.USD, 7)


def get_usd_bank_for_last_month(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.USD, 30)


def get_eur_bank_actual(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.Euro, 0)


def get_eur_bank_for_last_week(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.Euro, 7)


def get_eur_bank_for_last_month(update, context):
    send_message_to_user_based_on_input(update, context, SourceType.BANK, CurrencyType.Euro, 30)


def send_message_to_user_based_on_input_eur_and_dol(update, context):
    period = 14
    source = SourceType.BANK  # pick any source. Both sources contain (bank and exchange) contain NBU values
    data_dol = get_data_for_period(source, CurrencyType.USD, period)
    data_eur = get_data_for_period(source, CurrencyType.Euro, period)
    message = get_html_table_formatted_nbu(period, data_dol, data_eur)
    send_html_response(update, context, message)


def send_message_to_user_based_on_input(update, context, source_type: SourceType, currency: CurrencyType, period: int):
    data = get_data_for_period(source_type, currency, period)
    message = get_html_table_formatted(source_type, currency, period, data)
    send_html_response(update, context, message)


def send_html_response(update, context, message):
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message,
                             reply_markup=reply_keyboard_markup)
    logging.info(
        f"Sending response to: {update.message.chat_id} chat. Name: {update.message.chat.first_name} \
        LastName: {update.message.chat.last_name}")


def get_data_for_period(source_type: SourceType, currency: CurrencyType, period: int):
    today = date.today()

    data = [get_actual_data(source_type, currency)]
    for i in range(1, period):
        data.append(get_data_for_date_from_cache(source_type, currency, today - timedelta(days=i)))
    return data


def send_test_output_to_bot(update, context):
    data = [
        PageDataObject(10.10, 11.11, 10.22, date.today()),
        PageDataObject(10.12, 11.12, 10.32, date(2000, 12, 2)),
        PageDataObject(10.13, 11.16, 10.34, date(2000, 12, 3)),
        PageDataObject(10.14, 11.1, 10.12, date(2000, 12, 4)),
        PageDataObject(10.15, 11.2, 10.24, date(2000, 12, 5)),
        PageDataObject(10.16, 11.17, 10.32, date(2000, 12, 6)),
        PageDataObject(10.10, 11.1, 10.42, date(2000, 12, 1)),
        PageDataObject(10.12, 11.6, 10.32, date(2000, 12, 2)),
        PageDataObject(10.13, 11.4, 10.32, date(2000, 12, 3)),
        PageDataObject(10.14, 11.3, 10.31, date(2000, 12, 4)),
        PageDataObject(10.15, 11.3, 10.32, date(2000, 12, 5)),
        PageDataObject(10.16, 11.2, 10.37, date(2000, 12, 6)),
        PageDataObject(10.10, 11.1, 10.32, date(2000, 12, 1)),
    ]
    message = get_html_table_formatted(SourceType.EXCHANGER, CurrencyType.USD, len(data), data)
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)


def configure_updater(token_value):
    updater = Updater(token=token_value, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B12.get_value_escaped()), get_usd_exch_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B14.get_value_escaped()), get_usd_exch_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B22.get_value_escaped()), get_eur_exch_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B24.get_value_escaped()), get_eur_exch_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B32.get_value_escaped()), get_usd_bank_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B34.get_value_escaped()), get_usd_bank_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B42.get_value_escaped()), get_eur_bank_for_last_week))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B44.get_value_escaped()), get_eur_bank_for_last_month))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B51.get_value_escaped()), send_message_to_user_based_on_input_eur_and_dol))

    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B91.get_value_escaped()), show_help))
    dispatcher.add_handler(MessageHandler(Filters.regex(BotButton.B92.get_value_escaped()), show_link))

    dispatcher.add_handler(CommandHandler("test", send_test_output_to_bot))
    dispatcher.add_handler(CommandHandler("help", show_help))
    dispatcher.add_handler(CommandHandler("more", show_link))

    dispatcher.add_handler(MessageHandler(Filters.regex(".*"), default))
    dispatcher.add_error_handler(error)

    logging.debug(' Telegram dispatcher object was configured')
    updater.start_polling()
