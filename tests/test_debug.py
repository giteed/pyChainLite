# tests/test_debug.py
# Юнит-тест для модуля debug.py

import unittest
from io import StringIO
from unittest.mock import patch
from modules.debug import set_debug_mode, debug

class TestDebugModule(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_debug_output_enabled(self, mock_stdout):
        """
        Тестирует, что сообщение отладки выводится, когда отладка включена.
        """
        set_debug_mode(True)
        debug("Это тестовое сообщение")
        self.assertIn("Это тестовое сообщение", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_debug_output_disabled(self, mock_stdout):
        """
        Тестирует, что сообщение отладки не выводится, когда отладка выключена.
        """
        set_debug_mode(False)
        debug("Это тестовое сообщение")
        self.assertNotIn("Это тестовое сообщение", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
