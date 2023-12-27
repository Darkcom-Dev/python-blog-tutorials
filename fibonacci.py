def fibonacci(n):
  a = 1
  b = 0
  temp = 0

  while (n >= 0):
    temp = a
    a = a + b
    b = temp
    n = n - 1

  return b

# Create unit tests for fibonacci function
import unittest
class TestFibonacci(unittest.TestCase):
  def test_fibonacci(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(6), 8)
    self.assertEqual(fibonacci(7), 13)
    self.assertEqual(fibonacci(8), 21)
    self.assertEqual(fibonacci(9), 34)
    self.assertEqual(fibonacci(10), 55)
    self.assertEqual(fibonacci(11), 89)
    self.assertEqual(fibonacci(12), 144)
    self.assertEqual(fibonacci(13), 233)
    self.assertEqual(fibonacci(14), 377)
    self.assertEqual(fibonacci(15), 610)

  def test_fibonacci_negative(self):
    self.assertEqual(fibonacci(-1), 0)
    self.assertEqual(fibonacci(-2), 0)
    self.assertEqual(fibonacci(-3), 0)
    self.assertEqual(fibonacci(-4), 0)
    self.assertEqual(fibonacci(-5), 0)
    self.assertEqual(fibonacci(-6), 0)
    self.assertEqual(fibonacci(-7), 0)
    self.assertEqual(fibonacci(-8), 0)
    self.assertEqual(fibonacci(-9), 0)
    self.assertEqual(fibonacci(-10), 0)
    self.assertEqual(fibonacci(-11), 0)
    self.assertEqual(fibonacci(-12), 0)
    self.assertEqual(fibonacci(-13), 0)
    self.assertEqual(fibonacci(-14), 0)
    self.assertEqual(fibonacci(-15), 0)

  def test_fibonacci_zero(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 0)
    self.assertEqual(fibonacci(2), 0)
    self.assertEqual(fibonacci(3), 0)
    self.assertEqual(fibonacci(4), 0)
    self.assertEqual(fibonacci(5), 0)
    self.assertEqual(fibonacci(6), 0)
    self.assertEqual(fibonacci(7), 0)
    self.assertEqual(fibonacci(8), 0)
    self.assertEqual(fibonacci(9), 0)
    self.assertEqual(fibonacci(10), 0)
    self.assertEqual(fibonacci(11), 0)
    self.assertEqual(fibonacci(12), 0)
    self.assertEqual(fibonacci(13), 0)
    self.assertEqual(fibonacci(14), 0)
    self.assertEqual(fibonacci(15), 0)

  def test_fibonacci_negative_zero(self):
    self.assertEqual(fibonacci(-1), 0)
    self.assertEqual(fibonacci(-2), 0)
    self.assertEqual(fibonacci(-3), 0)
    self.assertEqual(fibonacci(-4), 0)
    self.assertEqual(fibonacci(-5), 0)
    self.assertEqual(fibonacci(-6), 0)
    self.assertEqual(fibonacci(-7), 0)
    self.assertEqual(fibonacci(-8), 0)
    self.assertEqual(fibonacci(-9), 0)
    self.assertEqual(fibonacci(-10), 0)
    self.assertEqual(fibonacci(-11), 0)
    self.assertEqual(fibonacci(-12), 0)
    self.assertEqual(fibonacci(-13), 0)
    self.assertEqual(fibonacci(-14), 0)
    self.assertEqual(fibonacci(-15), 0)

  def test_fibonacci_one(self):
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 1)
    self.assertEqual(fibonacci(4), 1)
    self.assertEqual(fibonacci(5), 1)
    self.assertEqual(fibonacci(6), 1)
    self.assertEqual(fibonacci(7), 1)
    self.assertEqual(fibonacci(8), 1)
    self.assertEqual(fibonacci(9), 1)
    self.assertEqual(fibonacci(10), 1)
    self.assertEqual(fibonacci(11), 1)
    self.assertEqual(fibonacci(12), 1)
    self.assertEqual(fibonacci(13), 1)
    self.assertEqual(fibonacci(14), 1)
    self.assertEqual(fibonacci(15), 1)

  def test_fibonacci_negative_one(self):
    self.assertEqual(fibonacci(-1), 0)
    self.assertEqual(fibonacci(-2), 0)
    self.assertEqual(fibonacci(-3), 0)
    self.assertEqual(fibonacci(-4), 0)
    self.assertEqual(fibonacci(-5), 0)
    self.assertEqual(fibonacci(-6), 0)
    self.assertEqual(fibonacci(-7), 0)
    self.assertEqual(fibonacci(-8), 0)
    self.assertEqual(fibonacci(-9), 0)
    self.assertEqual(fibonacci(-10), 0)
    self.assertEqual(fibonacci(-11), 0)
    self.assertEqual(fibonacci(-12), 0)
    self.assertEqual(fibonacci(-13), 0)
    self.assertEqual(fibonacci(-14), 0)
    self.assertEqual(fibonacci(-15), 0)

print(TestFibonacci.__doc__)