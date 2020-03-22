from datetime import date


class PageDataObject:
    "https://tables.finance.ua/ua/currency/cash/-/ua/usd/2/2020/03/20#3:0"
    def __init__(self, avg_rate: float, nbu_rate: float, date_obj: date):
        self.avg_rate = float(avg_rate)
        self.nbu_rate = float(nbu_rate)
        self.date_obj = date_obj
