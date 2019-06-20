from nose.tools import *

from projects.Text.pig_latin import case1, case2, case3

def test_case1():
    
    assert_equal(case1("bagel"), "agelbay")

"""def test_case2():
    pass"""

def test_case3():
    
    assert_equal(case3("another"), "otheranay")