from enum import Enum


class SourceType(Enum):
    EXCHANGER = 2
    BANK = 1

    def get_cyrylic_name(self):
        if self == self.EXCHANGER:
            return "обмінниках"
        elif self == self.BANK:
            return "банках"
        else:
            return "default"


if __name__ == '__main__':
    assert SourceType.EXCHANGER.get_cyrylic_name() == "обмінниках"
