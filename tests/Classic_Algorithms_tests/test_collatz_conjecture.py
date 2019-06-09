from nose.tools import *
from projects.Classic_Algorithms.collatz_conjecture import numberOfSteps

def test_numberOfSteps():
    assert_equal(numberOfSteps(3), 7)