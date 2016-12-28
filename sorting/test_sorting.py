import sorting
from random import randint


class TestClass:

    def setup_method(self, _):
        self._ls = []
        for ln in range(10, 1000, 100):
            self._ls.append([randint(0, x) for x in range(ln)])

    def teardown_method(self, _):
        del self._ls

    def test_builtin_sorted(self):
        for ls in self._ls:
            assert sorted(list(ls)) == sorted(ls)

    def test_merge_sort(self):
        for ls in self._ls:
            assert sorting.merge_sort(list(ls)) == sorted(ls)

    def test_insertion_sort(self):
        for ls in self._ls:
            assert sorting.insertion_sort(list(ls)) == sorted(ls)

    def test_bubble_sort(self):
        for ls in self._ls:
            assert sorting.bubble_sort(list(ls)) == sorted(ls)
