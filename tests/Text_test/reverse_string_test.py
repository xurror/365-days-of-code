from nose.tools import *

from projects.Text.reverse_string import reverse

def test_reverse():

    assert_equal(reverse("Hello, World!"), "!dlroW ,olleH")
