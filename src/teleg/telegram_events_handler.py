from datetime import timedelta, date

from telegram import ReplyKeyboardMarkup, ParseMode

from helper.formatted_output import get_html_table_preformated
from helper.tables_finance_page_parser import get_actual_data, get_data_for_date_from_cache
from model.CurrencyType import CurrencyType
from model.PageDataObject import PageDataObject
from model.SourceType import SourceType
from teleg.bot_constants import BotButton

index_message = '''
Курс валют в обмінниках України 🇺🇦
'''
help_message = '''
Позначення:
┣ обм. - Середній курс по обмінниках
┣ НБУ - Курс валют по Нац. Банку України
┗  √- Графічне відображення коливань
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


def test_output(update, context):
    data = [
        PageDataObject(1.0, 1, date(2000, 12, 1)),
        PageDataObject(1.2, 1, date(2000, 12, 2)),
        PageDataObject(1.3, 1, date(2000, 12, 3)),
        PageDataObject(1.4, 1, date(2000, 12, 4)),
        PageDataObject(1.5, 1, date(2000, 12, 5)),
        PageDataObject(1.6, 1, date(2000, 12, 6)),

        PageDataObject(1.0, 2, date(2000, 12, 1)),
        PageDataObject(1.2, 2, date(2000, 12, 2)),
        PageDataObject(1.3, 2, date(2000, 12, 3)),
        PageDataObject(1.4, 2, date(2000, 12, 4)),
        PageDataObject(1.5, 2, date(2000, 12, 5)),
        PageDataObject(1.6, 2, date(2000, 12, 6)),

        PageDataObject(1.0, 3, date(2000, 12, 1)),
        PageDataObject(1.2, 3, date(2000, 12, 2)),
        PageDataObject(1.3, 3, date(2000, 12, 3)),
        PageDataObject(1.4, 3, date(2000, 12, 4)),
        PageDataObject(1.5, 3, date(2000, 12, 5)),
        PageDataObject(1.6, 3, date(2000, 12, 6)),

        PageDataObject(1.0, 4, date(2000, 12, 1)),
        PageDataObject(1.2, 4, date(2000, 12, 2)),
        PageDataObject(1.3, 4, date(2000, 12, 3)),
        PageDataObject(1.4, 4, date(2000, 12, 4)),
        PageDataObject(1.5, 4, date(2000, 12, 5)),
        PageDataObject(1.6, 4, date(2000, 12, 6)),

        PageDataObject(1.0, 5, date(2000, 12, 1)),
        PageDataObject(1.2, 5, date(2000, 12, 2)),
        PageDataObject(1.3, 5, date(2000, 12, 3)),
        PageDataObject(1.4, 5, date(2000, 12, 4)),
        PageDataObject(1.5, 5, date(2000, 12, 5)),
        PageDataObject(1.6, 5, date(2000, 12, 6)),

        PageDataObject(1.0, 6, date(2000, 12, 1)),
        PageDataObject(1.2, 6, date(2000, 12, 2)),
        PageDataObject(1.3, 6, date(2000, 12, 3)),
        PageDataObject(1.4, 6, date(2000, 12, 4)),
        PageDataObject(1.5, 6, date(2000, 12, 5)),
        PageDataObject(1.6, 6, date(2000, 12, 6)),

        PageDataObject(1.0, 7, date(2000, 12, 1)),
        PageDataObject(1.2, 7, date(2000, 12, 2)),
        PageDataObject(1.3, 7, date(2000, 12, 3)),
        PageDataObject(1.4, 7, date(2000, 12, 4)),
        PageDataObject(1.5, 7, date(2000, 12, 5)),
        PageDataObject(1.6, 7, date(2000, 12, 6)),

        PageDataObject(1.0, 8, date(2000, 12, 1)),
        PageDataObject(1.2, 8, date(2000, 12, 2)),
        PageDataObject(1.3, 8, date(2000, 12, 3)),
        PageDataObject(1.4, 8, date(2000, 12, 4)),
        PageDataObject(1.5, 8, date(2000, 12, 5)),
        PageDataObject(1.6, 8, date(2000, 12, 6)),
    ]
    message = get_html_table_preformated(data)
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)
