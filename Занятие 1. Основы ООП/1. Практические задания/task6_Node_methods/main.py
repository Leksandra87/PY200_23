from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_
        ...  #  добавить атрибуты

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value
        ...  #  вернуть значение узла
    def get_next(self) -> Optional["Node"]:
        return self.next

    #  добавить метод get_next


if __name__ == '__main__':
    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел
    third_node = Node(3)
    print(first_node.get_value(), first_node.get_next())
    print(second_node.get_value(), second_node.get_next())
    print(third_node.get_value(), third_node.get_next())

    #  с помощью метода распечатать значение первого узла
    #  с помощью метода распечатать следующий узел второго узла
