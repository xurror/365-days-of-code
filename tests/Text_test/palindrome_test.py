from nose.tools import *

from projects.Text.palindrome import isPalindrome

def test_isPalindrome():

    assert_equal(isPalindrome('anna'), True)
    