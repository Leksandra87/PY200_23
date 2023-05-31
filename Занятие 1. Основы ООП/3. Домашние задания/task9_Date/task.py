class Date:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int):
            raise TypeError('Дата должна быть целым числом')
        self.day = day
        if not isinstance(month, int):
            raise TypeError('Номер месяца должен быть целым числом')
        self.month = month
        if not isinstance(year, int):
            raise TypeError('Год должен быть целым числом')
        self.year = year

    def __repr__(self) -> str:
        return f'Date({self.day:0>2}/{self.month:0>2}/{self.year:0>4})'

    def __str__(self) -> str:
        return f'{self.day:0>2}/{self.month:0>2}/{self.year:0>4}'


if __name__ == "__main__":
    d = Date(2, 4, 1865)
    print(d)
    print([Date(i, 5, 1965) for i in range(1, 6)])

#  class Date
