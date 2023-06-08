class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    #  какой декоратор следует применить?
    def is_leap_year(self, year: int) -> bool:
        """Проверяет, является ли год високосным"""
        ...  #  записать условие проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  #  вернуть количество дней указанного месяца

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        ...  #  если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    #  записать getter и setter для дня

    #  записать getter и setter для месяца

    #  записать getter и setter для года
