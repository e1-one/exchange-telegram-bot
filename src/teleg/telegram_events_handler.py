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
           ┣ обм. - Середній курс по обмінниках
           ┣ НБУ - Курс валют по Нац. Банку України
           ┗ G - Графік коливань
             ┣   '▏ ' - мінімум для заданого періоду
             ┗   '▉' - максимум для періоду
        '''

        custom_keyboard = [
            [BotButton.B11.value, BotButton.B12.value, BotButton.B13.value],
            [BotButton.B21.value, BotButton.B22.value, BotButton.B23.value]]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=False, selective=True)
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.MARKDOWN, text=message,
                                 reply_markup=reply_markup)
        self.value_analyzer.add_listener(UpdateListener(context, update.message.chat_id))

    def get_usd_actual(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.USD, 0)

    def get_usd_for_last_week(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.USD, 7)

    def get_usd_for_last_2_weeks(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.USD, 14)

    def get_eur_actual(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.Euro, 0)

    def get_eur_for_last_week(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.Euro, 7)

    def get_eur_for_last_2_weeks(self, update, context):
        self.get_currency_for_period(update, context, CurrencyType.Euro, 14)

    def get_currency_for_period(self, update, context, currency: CurrencyType, period: int):
        today = date.today()

        data = [get_actual_data(SourceType.EXCHANGER, currency)]
        for i in range(1, period):
            data.append(get_data_for_date_from_cache(SourceType.EXCHANGER, currency, today - timedelta(days=i)))

        message = get_html_table_preformated(data)
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode=ParseMode.HTML, text=message)
