import re
from enum import Enum


class BotButton(Enum):
    B12 = '$ 🏪 обмінники 7 днів'
    B14 = '$ 🏪 обмінники 30 днів'

    B22 = '€ 🏪 обмінники 7 днів'
    B24 = '€ 🏪 обмінники 30 днів'

    B32 = '$ 🏦 в банках 7 днів'
    B34 = '$ 🏦 в банках 30 днів'

    B42 = '€ 🏦 в банках 7 днів'
    B44 = '€ 🏦 в банках 30 днів'

    B51 = 'Курс НБУ $ i € до гривні за 14 днів'

    B91 = '❓ справка по боту'
    B92 = 'ℹ більше інформації'

    def get_value_escaped(self):
        return re.escape(self.value)


if __name__ == '__main__':
    print(BotButton.B11.get_value_escaped())
