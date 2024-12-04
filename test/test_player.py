from unittest.mock import patch
import unittest
from source.player import player_pon

class TestPlayerPon(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_gu(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_choki(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_pa(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")

if __name__ == '__main__':
    unittest.main()