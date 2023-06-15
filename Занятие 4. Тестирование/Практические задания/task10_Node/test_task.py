import unittest

from task import Node


class TestCase(unittest.TestCase):  #  наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        some_value = 5
        node = Node(some_value)
        self.assertIsNone(node.next)

        ...  #  с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        nod1 = Node(1)
        nod2 = Node(2, nod1)
        self.assertEqual(nod2.next, nod1)

        ...  #  проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        nod1 = Node(1)
        self.assertEqual(repr(nod1), 'Node(1, None)')

        ...  #  проверить метод __repr__ без следующего узла

    ...  #  пропустить тест с помощью декоратора unittest.skip
    @unittest.skip('Тест пропущен по заданию')
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        nod1 = Node(1)
        nod2 = Node(2, nod1)
        self.assertEqual(repr(nod2), 'Node(2, Node(1))')
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        self.assertEqual(str(node), f'{node.value}')

        #  проверить строковое представление

    def test_is_valid(self):
        nod1 = Node(1)
        self.assertIsNone(nod1.is_valid(nod1))
        self.assertTrue(nod1)
        ...  #  проверить метод is_valid при корректных узлах

        with self.assertRaises(TypeError):
            nod1.is_valid(20)
            nod = Node()
            nod.is_valid(nod)
        #  с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
