import unittest
from prime_factorisation import prime

class test_pi(unittest.TestCase):
    """def setUp(self):
        pass"""

    def test_dp(self):
        self.assertEqual(prime(7), True)

if __name__ == "__main__":
    try:
        unittest.main()
    
    except AssertionError as e:
        print(e)