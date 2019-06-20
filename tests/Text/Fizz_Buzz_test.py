from nose.tools import *

from projects.Text.Fizz_Buzz import fizz, buzz

def test_fizz():

    assert_equal(fizz(3), True)
    assert_equal(fizz(7), False)

def test_buzz():

    assert_equal(buzz(10), True)
    assert_equal(buzz(9), False)
