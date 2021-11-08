from driving_func import amount, checkpoint
import unittest

class TestCollatzConjecture(unittest.TestCase):
  """
  Class for testing Collatz Conjecture.
  """

  def test_amount(self):
    """
    Example of testing for add_one function

    You do not need to further test add_one
    """
    self.assertEqual(amount(5), 5000)
    self.assertEqual(amount(8), 15000)
    self.assertEqual(amount(15), 1000000)
    self.assertEqual(amount(3), 2000)
    
  def test_checkpoint(self):
      self.assertEqual(checkpoint(4),0)
      self.assertEqual(checkpoint(7),5000)
    


if __name__ == '__main__':
    unittest.main()
