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

        self.is_valid_date(self._day, self._month, self._year)

    #  какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
        ...  # записать условие проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

        ...  # вернуть количество дней указанного месяца

    def is_valid_date(self, day: int, month: int, year: int) -> None:
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
        ...  # если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError
        if not 0 < day < 32:
            raise ValueError
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError
        if not 0 < month < 13:
            raise ValueError
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError
        if year < 1:
            raise ValueError
        self._year = year

    def __str__(self) -> str:
        return f'{self.day:0>2}/{self.month:0>2}/{self.year:0>4}'
    #  записать getter и setter для дн

    #  записать getter и setter для месяца

    #  записать getter и setter для года


if __name__ == "__main__":
    date = Date(22, 2, 2013)
    print(date)
