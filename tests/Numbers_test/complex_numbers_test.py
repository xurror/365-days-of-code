from nose.tools import *
from projects.Numbers.complex_numbers import *

def test_addComplex():
    assert_equal(addComplex(1+2j, 2+1j), (3+3j))

def test_multComplex():
    assert_equal(multComplex(2j, 3j), -6)

def test_invertComplex():
    assert_equal(invertComplex(2+2j), (1-1j)/4)

def test_negateComplex():
    assert_equal(negateComplex(2j), -2j)