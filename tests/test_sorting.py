from sorting import merge_sort, insertion_sort, bubble_sort
from random import randint


class TestClass:

    def setup_method(self, _):
        self._ls = []
        for ln in range(10, 1000, 100):
            self._ls.append([randint(0, x) for x in range(ln)])

    def teardown_method(self, _):
        del self._ls

    def test_merge_sort(self):
        for ls in self._ls:
            assert merge_sort(list(ls)) == sorted(ls)

    def test_insertion_sort(self):
        for ls in self._ls:
            assert insertion_sort(list(ls)) == sorted(ls)

    def test_bubble_sort(self):
        for ls in self._ls:
            assert bubble_sort(list(ls)) == sorted(ls)
