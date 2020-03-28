from enum import Enum


class CurrencyType(Enum):
    Euro = 'eur'
    USD = 'usd'

    def get_symbol(self):
        if self == self.Euro:
            return "€"
        elif self == self.USD:
            return "$"
        else:
            return "default"
