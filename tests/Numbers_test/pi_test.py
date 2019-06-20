from nose.tools import *
from projects.Numbers.prime_factorisation import prime1, prime2

def test_dp():

    assert_equal(prime1(7), True)
    assert_equal(prime2(7), True)