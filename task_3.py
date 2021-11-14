class Cellular:
    __count: int

    def __init__(self, cell_count: int):
        assert cell_count > 0, "Количество ячеек должно быть больше 0"
        self.__count = cell_count

    def __add__(self, other: 'Cellular'):
        self.validate_item(other)
        return Cellular(self.__count + other.__count)

    def __sub__(self, other: 'Cellular'):
        self.validate_item(other)
        return Cellular(self.__count - other.__count)

    def __mul__(self, other: 'Cellular'):
        self.validate_item(other)
        return Cellular(self.__count * other.__count)

    def __truediv__(self, other: 'Cellular'):
        self.validate_item(other)
        return Cellular(self.__count // other.__count)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Операции допустимы только между клетками"

    @property
    def count(self) -> int:
        return self.__count

    def make_order(self, count_per_row: int):
        item = "*" * self.__count
        result = ""
        count_lines = len(item) // count_per_row
        for i in range(count_lines):
            ind = i*count_per_row
            result += f"{item[ind: ind + count_per_row]}\n"

        if count_lines != len(item) / count_per_row:
            result += f"{'*' * (len(item) - count_lines * count_per_row)}\n"

        return result


first = Cellular(17)
second = Cellular(2)
res = (first * second)
print(res)
print(res.make_order(6))