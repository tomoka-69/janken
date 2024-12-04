import unittest
from unittest.mock import patch
from io import StringIO
import source.player
import source.computer
import source.janken_judge
import source.janken_main

from test_janken_judge import main

class TestMainFunctionWin(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('source.computer.computer_pon', side_effect=['チョキ', 'パー', 'グー'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_game(self, mock_stdout, mock_computer_pon, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("あなたの勝ちです！", output)
        
class TestMainFunctionDrow(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('source.computer.computer_pon', side_effect=['グー', 'チョキ', 'パー'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_game(self, mock_stdout, mock_computer_pon, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("あいこです！再度対決！", output)

class TestMainFunctionLose(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('source.computer.computer_pon', side_effect=['パー', 'グー', 'チョキ'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_game(self, mock_stdout, mock_computer_pon, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("コンピュータの勝ちです！", output)

if __name__ == '__main__':
    unittest.main()