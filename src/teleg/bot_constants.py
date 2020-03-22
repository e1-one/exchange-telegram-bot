import re
from enum import Enum


class BotButton(Enum):
    B11 = 'Курс $ в обм. зараз'
    B12 = '$ за 7 днів'
    B13 = '$  за 14 днів'
    B21 = 'Курс € в обм. зараз'
    B22 = '€ за 7 днів'
    B23 = '€ за 14 днів'

    def get_value_escaped(self):
        return re.escape(self.value)

if __name__ == '__main__':
    print(BotButton.B11.get_value_escaped())
