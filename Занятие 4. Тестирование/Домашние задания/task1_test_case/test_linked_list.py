import unittest
from linked_list import LinkedList

LL = ['first', 'second', 'third']


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """ Устанавливаем данные для тестирования """
        self.my_list = LinkedList(LL)

    def test_init(self):
        """ Проверяет корректность формирования атрибутов связанного списка при инициализации"""
        self.assertEqual(self.my_list.len, 3)
        self.assertEqual(self.my_list.head.value, LL[0])
        self.assertEqual(self.my_list.tail.value, LL[-1])

    def test_append(self):
        """ Проверяем метод 'append' """
        new_tail = 'tail'
        self.my_list.append(new_tail)
        self.assertEqual(self.my_list.tail.value, new_tail)

    def test_step_by_step(self):
        """ Проверяем метод 'step_by_step_on_nodes' """
        index = 1
        self.assertEqual(self.my_list.step_by_step_on_nodes(index).value, LL[index])

    def test_getitem(self):
        """ Проверяем метод 'getitem' """
        index = 1
        self.assertEqual(self.my_list.__getitem__(index), LL[index])

    def test_setitem(self):
        """ Проверяем метод 'setitem' """
        index = 1
        value = 'кумкват'
        self.my_list.__setitem__(index, value)
        self.assertEqual(self.my_list.__getitem__(index), value)

    def test_to_list(self):
        """ Проверяем метод 'to_list' """
        self.assertEqual(self.my_list.to_list(), LL)

    def test_repr(self):
        """ Проверяем метод 'repr' """
        self.assertEqual(repr(self.my_list), f"{self.my_list.__class__.__name__}({self.my_list.to_list()})")

    def test_str(self):
        """ Проверяем метод 'str' """
        self.assertEqual(str(self.my_list), f"{self.my_list.to_list()}")

    def test_add(self):
        """ Проверяем метод 'add' """
        other_list = ['1', '2', '3']
        ll = LL
        self.my_list = self.my_list + LinkedList(other_list)
        self.assertEqual(self.my_list.to_list(), ll + other_list)


if __name__ == '__main__':
    unittest.main()
