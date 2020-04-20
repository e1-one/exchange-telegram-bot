def map_value(x: float, in_min: float, in_max: float, out_min: float, out_max: float):
    if in_max == in_min:
        return 0
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def unique(list1):
    list_set = set(list1)
    return list(list_set)


class ValuesToGraphBlockTranslator:
    squares = ['▏', '▎', '▍', '▋', '▊', '▉']
    no_data = '▁'

    def __init__(self, values: list):
        sorted_values = sorted(unique(values))

        self.min = sorted_values[0] if sorted_values[0] != 0 else sorted_values[1]
        self.max = sorted_values[len(sorted_values)-1]

    def get(self, value: float):
        if value == 0:
            return ValuesToGraphBlockTranslator.no_data
        index = int(map_value(value, self.min, self.max, 0, len(ValuesToGraphBlockTranslator.squares) - 1))
        return ValuesToGraphBlockTranslator.squares[index]


