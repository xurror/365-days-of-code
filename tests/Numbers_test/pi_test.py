from nose.tools import *
from projects.Numbers.prime_factorisation import prime

def test_dp():
    assert_equal(prime(7), True)