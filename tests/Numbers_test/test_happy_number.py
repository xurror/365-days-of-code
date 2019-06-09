from nose.tools import *
from projects.Numbers.happy_numbers import isHappyNumber

def test_isHappyNumber():
    assert_equal(isHappyNumber('998'), True)