import re
from enum import Enum


class BotButton(Enum):
    B12 = '$ 🏪 7 днів'
    B13 = '$ 🏪 14 днів'
    B14 = '$ 🏪 30 днів'

    B22 = '€ 🏪 7 днів'
    B23 = '€ 🏪 14 днів'
    B24 = '€ 🏪 30 днів'

    B32 = '$ 🏦 7 днів'
    B33 = '$ 🏦 14 днів'
    B34 = '$ 🏦 30 днів'

    B42 = '€ 🏦 7 днів'
    B43 = '€ 🏦 14 днів'
    B44 = '€ 🏦 30 днів'

    B91 = '❓ допомога'
    B92 = 'ℹ посилання на finance.ua, bank.gov.ua'

    def get_value_escaped(self):
        return re.escape(self.value)


if __name__ == '__main__':
    print(BotButton.B11.get_value_escaped())
