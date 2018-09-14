import unittest

from DayFour2 import power

class test_DayFour2(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3,4),81)



if __name__ == '__main__':  
    unittest.main()



 