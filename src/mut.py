import unittest
from hypothesis import given
import hypothesis.strategies as st
from p1 import *
class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(List().size(), 0)
        self.assertEqual(List('a').size(), 1)
        list = List('a')
        list.add_to_tail('b')
        self.assertEqual(list.size(), 2)

    def test_empty(self):

        self.assertEqual(List('a').isEmpty(),False )
        list = List('a')
        list.add_to_tail('b')
        self.assertEqual(list.isEmpty(), False)

    def test_get(self):
        list = List('a')
        list.add_to_tail('b')
        self.assertEqual(list.get(0),'a')
        self.assertEqual(list.get(1), 'b')

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        
        for e in test_data:
            lst = List()
            lst.from_list(e)
            self.assertEqual(lst.lt, e)
    def test_add_to_head(self):
        lst = List()
        self.assertEqual(lst.lt, [])
        lst.add_to_head('a')
        self.assertEqual(lst.lt, ['a'])
        lst.add_to_head('b')
        self.assertEqual(lst.lt, ['b', 'a'])

    def test_add_to_tail(self):
        lst = List()
        self.assertEqual(lst.lt, [])
        lst.add_to_tail('a')
        self.assertEqual(lst.lt, ['a'])
        lst.add_to_tail('b')
        self.assertEqual(lst.lt, ['a', 'b'])

    def test_map(self):
        lst = List()
        lst.map(str)
        self.assertEqual(lst.lt, [])
        lst = List()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.lt, ["1", "2", "3"])

    def test_reduce(self):  # sum of empty list
        lst = List()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = List()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = List()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())
    def test_findall(self):
        list = List('a')
        list.add_to_tail('b')
        list.add_to_tail('c')
        list.add_to_tail('b')
        self.assertEqual(list.findAll('b'),[1,3] )


    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = List()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

if __name__ == '__main__':
    unittest.main()