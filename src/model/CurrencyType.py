from enum import Enum


class CurrencyType(Enum):
    Euro = 'eur'
    USD = 'usd'

if __name__ == '__main__':
    print(CurrencyType.USD.value)
