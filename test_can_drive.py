import unittest
def can_drive(age):
    driving_age = 16
    return age >= driving_age
 
class TestCanDrive(unittest.TestCase):

    def test_underage(self):
        self.assertFalse(can_drive(15))

    def test_minimum_age(self):
        self.assertTrue(can_drive(16))

    def test_above_age(self):
        self.assertTrue(can_drive(20))

    def test_zero_age(self):
        self.assertFalse(can_drive(0))

    def test_negative_age(self):
        self.assertFalse(can_drive(-5))

if __name__ == '__main__':
    unittest.main()
