from unittest import TestCase
import primes


class TestPrimes(TestCase):
    def test_cprimes(self):
        result = primes.cprimes(10)
        self.assertEquals(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
