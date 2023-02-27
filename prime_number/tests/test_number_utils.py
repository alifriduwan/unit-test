from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
  def test_give_1_2_3_is_prime(self):
      prime_list = [1, 2, 3]
      is_prime = is_prime_list(prime_list)
      self.assertTrue(is_prime)
  def test_give_2_4_6_is_not_prime(self):
      prime_list = [2, 4, 6]
      is_prime = is_prime_list(prime_list)
      self.assertFalse(is_prime)

  def test_two_num_in_list_is_prime(self):
      prime_list = [5,17,23]
      is_prime = is_prime_list(prime_list)
      self.assertTrue(is_prime)

  def test_two_num_in_list_is_not_prime(self):
      prime_list = [9,12,23]
      is_prime = is_prime_list(prime_list)
      self.assertFalse(is_prime)

  def test_two_num_in_list_is_not_prime(self):
      prime_list = [9,12,23]
      is_prime = is_prime_list(prime_list)
      self.assertFalse(is_prime)

  def test_all_in_list_is_primes(self): 
        prime_list = [17,19,23]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)


          

