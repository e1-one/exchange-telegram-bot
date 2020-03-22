import logging
from functools import lru_cache
from threading import Timer

from lxml import html
from datetime import date
import requests

from model.CurrencyType import CurrencyType
from model.PageDataObject import PageDataObject
from model.SourceType import SourceType

def get_data_from_html_page(source_type: SourceType, currency_type: CurrencyType, for_date: date):
    url = f"https://tables.finance.ua/ua/currency/cash/-/ua/{currency_type.value}/{source_type.value}/{for_date.year}/{for_date.month}/{for_date.day}"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    avg_rate_value = tree.xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[5]/div[1]/table/tr[2]/td[2]/*')[0].text
    avg_nbu_value = tree.xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[5]/div[1]/table/tr[3]/td/text()')[0]
    return PageDataObject(avg_rate_value, avg_nbu_value, for_date)


class LatestDataContainer:
    def __init__(self):
        self.self_scheduled_task()

    def self_scheduled_task(self):
        Timer(60 * 15, self.self_scheduled_task).start()
        self.latest_data_usd = get_data_from_html_page(SourceType.EXCHANGER, CurrencyType.USD, date.today())
        self.latest_data_eur = get_data_from_html_page(SourceType.EXCHANGER, CurrencyType.Euro, date.today())
        logging.info(f"self_scheduled_task invoked. Latest data is: $ avg: {self.latest_data_usd.avg_rate} € avg: {self.latest_data_eur.avg_rate}")


latest = LatestDataContainer()


def get_actual_data(source_type: SourceType, currency_type: CurrencyType):
    if (source_type == SourceType.EXCHANGER) & (currency_type == CurrencyType.USD):
        return latest.latest_data_usd
    elif (source_type == SourceType.EXCHANGER) & (currency_type == CurrencyType.Euro):
        return latest.latest_data_eur
    else:
        raise RuntimeError('Have no data for this input')


@lru_cache(maxsize=None)
def get_data_for_date_from_cache(source_type: SourceType, currency_type: CurrencyType, for_date: date):
    return get_data_from_html_page(source_type, currency_type, for_date)


if __name__ == '__main__':
    print(get_actual_data(SourceType.EXCHANGER, CurrencyType.USD))
    print(get_actual_data(SourceType.EXCHANGER, CurrencyType.USD))
    print(get_actual_data(SourceType.EXCHANGER, CurrencyType.USD))
