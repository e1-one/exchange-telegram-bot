from datetime import date
from typing import List

from helper.values_to_graph_block_translator import ValuesToGraphBlockTranslator
from model.page_data_object import PageDataObject


def get_html_table_preformated(list_el: List[PageDataObject]):
    return f"<pre>{get_str_table(list_el)}</pre>"


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
    # qwertyuiopasdfghjklzxcvbnm1234567890q
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


if __name__ == '__main__':
    fout = get_str_table([
        PageDataObject(1.1, 100, date(2000, 12, 1)),
        PageDataObject(1.2, 1, date(2000, 12, 2)),
        PageDataObject(1.3, 1, date(2000, 12, 3)),
        PageDataObject(1.4, 1, date(2000, 12, 4)),
        PageDataObject(1.5, 1, date(2000, 12, 5)),
        PageDataObject(1.6, 1, date(2000, 12, 6)),
        PageDataObject(1.7, 1, date(2000, 12, 7)),

    ])
    print(fout)
