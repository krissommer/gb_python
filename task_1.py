class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract_numbers(date_string)
        self.validate_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def extract_numbers(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "Неверный формат числа"
        assert 1 <= m <= 12, "Неверный формат месяца"
        assert 1970 <= y <= 2100, "Неверный формат года"


my_date = Date('19-12-2001')
# my_date = Date('24-00-2001')  # error
# my_date = Date('24-13-2001')  # error
# my_date = Date('24-13-2101')  # error