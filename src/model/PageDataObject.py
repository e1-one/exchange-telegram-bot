from datetime import date


class PageDataObject:

    def __init__(self, avg_rate: float, nbu_rate: float, date_obj: date):
        self.avg_rate = float(avg_rate)
        self.nbu_rate = float(nbu_rate)
        self.date_obj = date_obj
