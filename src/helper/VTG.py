
class VTG:
    squares = ['▏', '▎', '▍', '▋', '▊', '▉']

    def __init__(self, values: list):
        self.max = max(values)
        self.min = min(values)

    def get(self, value: float):
        index = int(map(value, self.min, self.max, 0, len(VTG.squares) - 1))
        return VTG.squares[index]


def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float):
    if (in_max == in_min):
        return 0
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
