from datetime import timedelta, date

from telegram import ReplyKeyboardMarkup, ParseMode

from helper.formatted_output import get_html_table_preformated
from helper.tables_finance_page_parser import get_actual_data, get_data_for_date_from_cache
from model.CurrencyType import CurrencyType
from model.PageDataObject import PageDataObject
from model.SourceType import SourceType
from teleg.bot_constants import BotButton

import logging

index_message = '''
Курс валют в обмінниках України 🇺🇦
'''
help_message = '''
Позначення:
┣ купів. - середній курс купівлі валюти по обмінниках
┣ продаж - середній курс продажі валюти по обмінниках
┣ НБУ - Курс валют по Національному Банку України
┗  √- колонка відображення коливань курсу, де:
  ┣   '▏ ' - мінімум для заданого періоду
  ┗   '▉' - максимум для періоду
'''
link = '''
https://tables.finance.ua/ua/currency/cash/-/ua,0,7oiylpmiow8iy1smadi/usd/2#3:0
'''


def start(update, context):
    custom_keyboard = [
        [BotButton.B11.value, BotButton.B12.value, BotButton.B13.value, BotButton.B14.value],
        [BotButton.B21.value, BotButton.B22.value, BotButton.B23.value, BotButton.B14.value],
        [BotButton.B31.value, BotButton.B32.value],
    ]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=False, selective=True)
    logging.info(f"{update.message.chat_id} chat. Name: {update.message.chat.first_name} LastName: {update.message.chat.last_name} called /start command")
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=index_message,
                             reply_markup=reply_markup)


def show_help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=help_message)


def show_link(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=link)


def get_usd_actual(update, context):
    get_currency_for_period(update, context, CurrencyType.USD, 0)


def get_usd_for_last_week(update, context):
    get_currency_for_period(update, context, CurrencyType.USD, 7)


def get_usd_for_last_2_weeks(update, context):
    get_currency_for_period(update, context, CurrencyType.USD, 14)


def get_usd_for_last_month(update, context):
    get_currency_for_period(update, context, CurrencyType.USD, 31)


def get_eur_actual(update, context):
    get_currency_for_period(update, context, CurrencyType.Euro, 0)


def get_eur_for_last_week(update, context):
    get_currency_for_period(update, context, CurrencyType.Euro, 7)


def get_eur_for_last_2_weeks(update, context):
    get_currency_for_period(update, context, CurrencyType.Euro, 14)


def get_eur_for_last_month(update, context):
    get_currency_for_period(update, context, CurrencyType.Euro, 31)


def get_currency_for_period(update, context, currency: CurrencyType, period: int):
    today = date.today()

    data = [get_actual_data(SourceType.EXCHANGER, currency)]
    for i in range(1, period):
        data.append(get_data_for_date_from_cache(SourceType.EXCHANGER, currency, today - timedelta(days=i)))

    message = get_html_table_preformated(data)
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)
    logging.info(f"{update.message.chat_id} chat. Name: {update.message.chat.first_name} LastName: {update.message.chat.last_name}: received response with currency table")


def test_output(update, context):
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
    message = get_html_table_preformated(data)
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)
