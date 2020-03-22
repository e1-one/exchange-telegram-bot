from datetime import timedelta, date

from telegram import ReplyKeyboardMarkup, ParseMode

from helper.formatted_output import get_html_table_preformated
from helper.tables_finance_page_parser import get_actual_data, get_data_for_date_from_cache
from model.CurrencyType import CurrencyType
from model.SourceType import SourceType
from teleg.bot_constants import BotButton
from teleg.listener import UpdateListener


class EventHandler:

    def __init__(self, value_analyzer) -> None:
        super().__init__()
        self.value_analyzer = value_analyzer

    def start(self, update, context):
        message = '''
        Я бот який показує історію курсу валют в обмінниках києва.
        Позначення:
            обм. - Середній курс по обмінниках
            НБУ - Курс валют по Нац. Банку України
            G - Графік коливань
                '▏ ' - мінімум для заданого періоду
                '▉' - максимум 
        '''

        custom_keyboard = [
            [BotButton.B11.value, BotButton.B12.value, BotButton.B13.value],
            [BotButton.B21.value, BotButton.B22.value, BotButton.B23.value]]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=False, selective=True)
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=message,
                                 reply_markup=reply_markup)
        self.value_analyzer.add_listener(UpdateListener(context, update.message.chat_id))

    def get_usd(self, update, context):
        data = get_actual_data(SourceType.EXCHANGER, CurrencyType.USD)
        message = get_html_table_preformated([data])
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)

    def get_usd_for_last5_days(self, update, context):
        today = date.today()

        # index_message = f"Nbu rate is: {data.nbu_rate}. Avg rate is: {data.avg_rate}"
        message = get_html_table_preformated([
            get_actual_data(SourceType.EXCHANGER, CurrencyType.USD),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=1)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=2)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=3)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=4)),
        ])
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)

    def get_usd_for_last_2_weeks(self, update, context):
        today = date.today()

        # index_message = f"Nbu rate is: {data.nbu_rate}. Avg rate is: {data.avg_rate}"
        message = get_html_table_preformated([
            get_actual_data(SourceType.EXCHANGER, CurrencyType.USD),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=1)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=2)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=3)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=4)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=5)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=6)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=7)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=8)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=9)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=10)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=11)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=12)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=13)),
            get_data_for_date_from_cache(SourceType.EXCHANGER, CurrencyType.USD, today - timedelta(days=14)),

        ])
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)
