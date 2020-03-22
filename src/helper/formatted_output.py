from datetime import date
from typing import List

from tabulate import tabulate

from helper.VTG import VTG
from model.PageDataObject import PageDataObject


def get_html_table_preformated(list_el: List[PageDataObject]):
    return f"<pre>{get_str_table(list_el)}</pre>"


def get_str_table(list_el: List[PageDataObject]):
    list_avg = []
    list_nbu = []
    for e in list_el:
        list_avg.append(e.avg_rate)
        list_nbu.append(e.nbu_rate)

    vtg_avg = VTG(list_avg)
    vtg_nbu = VTG(list_nbu)

    table = []
    for el in list_el:
        table.append([date_format(el.date_obj), el.avg_rate, vtg_avg.get(el.avg_rate), el.nbu_rate, vtg_nbu.get(el.nbu_rate)])
    tabular_output = tabulate(table, headers=["Дата", "обм.", "G", "НБУ", "G"], tablefmt="simple")
    return tabular_output


def date_format(for_date):
    if for_date == date.today():
        return "Сьогодні"
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
