import unittest

from DayFour1 import sum

class test_DayFour1(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([8,  2,  3,  0,  7]),20)

if __name__ == '__main__':
    unittest.main()
      

     