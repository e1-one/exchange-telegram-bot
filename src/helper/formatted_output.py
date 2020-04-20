from datetime import date
from typing import List

from helper.values_to_graph_block_translator import ValuesToGraphBlockTranslator
from model.currency_type import CurrencyType
from model.page_data_object import PageDataObject
from model.source_type import SourceType


def get_html_table_formatted(source_type: SourceType, currency: CurrencyType, period: int, list_el: List[PageDataObject]):
    return f"""
<pre>Курс {currency.get_symbol()} в {source_type.get_cyrylic_name()} за {period} днів
----------------------------------
{get_str_table(list_el)}</pre>
"""


def get_str_table(list_el: List[PageDataObject]):
    list_avg_sell = []
    list_avg_buy = []
    list_nbu = []
    for e in list_el:
        list_avg_sell.append(e.avg_sell_rate)
        list_avg_buy.append(e.avg_buy_rate)
        list_nbu.append(e.nbu_sell_rate)

    vtg_avg_sell = ValuesToGraphBlockTranslator(list_avg_sell)
    vtg_avg_buy = ValuesToGraphBlockTranslator(list_avg_buy)
    vtg_nbu = ValuesToGraphBlockTranslator(list_nbu)

    l1 = "Дата   купів. √  продаж √   НБУ  √\n"
    l2 = "-----  ------ -  ------ -  ----- -\n"
    message = l1 + l2
    format_pattern = "{0:5s}  {1:6.2f} {2:1s}  {3:6.2f} {4:1s}  {5:5.2f} {6:1s}\n"

    for el in list_el:
        message += format_pattern.format(
            date_format(el.date_obj),
            el.avg_buy_rate,
            vtg_avg_buy.get(el.avg_buy_rate),
            el.avg_sell_rate,
            vtg_avg_sell.get(el.avg_sell_rate),
            el.nbu_sell_rate,
            vtg_nbu.get(el.nbu_sell_rate))
    return message


def date_format(for_date):
    if for_date == date.today():
        return "Сьог."
    else:
        return for_date.strftime('%d/%m')
