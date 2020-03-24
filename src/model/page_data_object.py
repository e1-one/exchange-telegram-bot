from datetime import date


class PageDataObject:

    def __init__(self, avg_sell_rate, avg_buy_rate, nbu_rate, date_obj: date):
        self.avg_sell_rate = float(avg_sell_rate)
        self.avg_buy_rate = float(avg_buy_rate)
        self.nbu_sell_rate = float(nbu_rate)
        self.date_obj = date_obj
