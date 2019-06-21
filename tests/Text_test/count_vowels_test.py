from nose.tools import *

from projects.Text.count_vowels import count_vowel

def test_count_vowel():

    assert_equal(count_vowel("Hello World"), 3)
    