from nose.tools import *
from projects.Numbers.factorial_finder import recursive

def test_recursive():
    assert_equal(recursive(3), 6)