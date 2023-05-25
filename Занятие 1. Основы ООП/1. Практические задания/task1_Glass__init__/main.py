from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        if occupied_volume > capacity_volume:
            raise ValueError('Объм вмещаемой жидкости не может быть больше объема стакана')
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        #   инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass(500, 50)
    print(glass_1.occupied_volume)
    print(glass_2.capacity_volume)

    ...  # инициализировать два объекта типа Glass

    #  попробовать инициализировать не корректные объекты
