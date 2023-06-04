class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @classmethod
    def is_leap_year(cls, year: int):
        """Проверяет, является ли год високосным"""
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
        ...  # реализовать метод

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

            ...  # используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError
        if self.is_leap_year(year):
            if not 0 < day <= self.DAY_OF_MONTH[1][month - 1]:
                raise ValueError
        elif not self.is_leap_year(year):
            if not 0 < day <= self.DAY_OF_MONTH[0][month - 1]:
                raise ValueError
        if not 0 < month <= 12:
            raise ValueError
        if year <= 0:
            raise ValueError
        ...  # проверить валидность даты

    def __str__(self) -> str:
        return f'{self.day:0>2}/{self.month:0>2}/{self.year:0>4}'


if __name__ == "__main__":
    date = Date(28, 2, 2013)
    print(date)
