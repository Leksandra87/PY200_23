from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.len:
            raise ValueError
        if index == 0:
            if self.len == 1:
                self.step_by_step_on_nodes(0).value = None
                self.step_by_step_on_nodes(0).next = None
                self.len = 0
            else:
                self.head = self.step_by_step_on_nodes(1)
                self.len -= 1
        elif index == self.len - 1:
            self.step_by_step_on_nodes(self.len - 2).next = None
            self.len -= 1
        else:
            self.step_by_step_on_nodes(index - 1).next = self.step_by_step_on_nodes(index + 1)
            self.len -= 1

    def list_count(self, value: Any) -> int:
        return len([linked_list_value for linked_list_value in self if linked_list_value == value])

    def list_index(self, value: Any) -> int:
        return self.to_list().index(value)

    def list_extend(self, data: Iterable):
        if data is not None:
            for value in data:
                self.append(value)

    def list_pop(self, index: int = None) -> Any:
        if not isinstance(index, (int, type(None))):
            raise TypeError
        if not index:
            last_value = self.step_by_step_on_nodes(self.len - 1).value
            self.__delitem__(self.len - 1)
            return last_value
        elif not 0 < index < self.len - 1:
            raise ValueError
        else:
            value = self.step_by_step_on_nodes(index).value
            self.__delitem__(index)
            return value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5]
    linked_list = LinkedList(list_)
    print(linked_list)
    print(linked_list.list_pop(2))
    print(linked_list)
    print(linked_list.list_pop())
    print(linked_list)
