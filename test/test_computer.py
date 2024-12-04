import unittest
from source.computer import computer_pon

class TestComputerPon(unittest.TestCase):

    def test_computer_pon(self):
        expected_hands = ["グー", "チョキ", "パー"]

        for _ in range(100):
            result = computer_pon()
            self.assertIn(result, expected_hands)

if __name__ == '__main__':
    unittest.main()