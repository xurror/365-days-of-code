from nose.tools import *
from projects.Classic_Algorithms.sorting.bubble_sort import bubbleSort

def test_bubbleSort():
    assert_equal(bubbleSort("4, 5, 9, 2, 6, 1, 8, 3, 7"), [1, 2, 3, 4, 5, 6, 7, 8, 9])
