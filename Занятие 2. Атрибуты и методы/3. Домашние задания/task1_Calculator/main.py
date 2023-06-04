class Calculator:
    """
    Класс - калькулятор, который только умножает и складывает
    """
    @staticmethod
    def add(*args):
        """
        Сложение
        """
        return sum(i for i in args)
    @staticmethod
    def mul(*args):
        """
        Умножение
        """
        m = 1
        for i in args:
            m *= i
        return m
    ...  #  написать статические методы


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
