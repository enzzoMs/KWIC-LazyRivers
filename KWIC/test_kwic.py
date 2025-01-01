import unittest
import kwic
from unittest.mock import mock_open, patch
from textwrap import dedent

class TestKWIC(unittest.TestCase):
    
    def test_read_lines_from_file(self):
        sample_file_text = dedent(
            """O cachorro late alegremente.
            O gato é bonito.
            Brilhar como o sol é o desejo de muitos."""
        );

        with patch("builtins.open", mock_open(read_data=sample_file_text)) as mock_open_file:
            test_file_path = "test.txt"
            expected_lines = [line.strip() for line in sample_file_text.splitlines()]

            read_lines = list(kwic.read_lines_from_file(test_file_path))

            mock_open_file.assert_called_once_with(test_file_path, "r", encoding="utf-8")
            self.assertEqual(read_lines, expected_lines)
        
    def test_read_get_words_in_line(self):
        test_line = "O cachorro late alegremente."
        expected_words = test_line.split();

        words = list(kwic.get_words_in_line(test_line))

        self.assertEqual(words, expected_words)

    def test_find_keywords_in_line(self):
        test_line = "O cachorro late alegremente."
        expected_keywords = [
            ("cachorro", test_line), ("late", test_line), ("alegremente.", test_line)
        ]

        keywords = list(kwic.find_keywords_in_line(test_line))

        self.assertEqual(keywords, expected_keywords)

    def test_highlight_keyword_in_line(self):
        test_line = "O sol é uma estrela."
        test_keyword = "estrela."
        expected_result = "estrela. O sol é uma"

        keyword_in_context = kwic.highlight_keyword_in_line(test_keyword, test_line)
        
        self.assertEqual(keyword_in_context, expected_result)

    def test_generate_kwic(self):
        test_line = "O sol é uma estrela."
        expected_kwic = [
            ("sol é uma estrela. O", test_line),
            ("estrela. O sol é uma", test_line)
        ]

        with patch("builtins.open", mock_open(read_data=test_line)):
            test_file_path = "test.txt"

            kwic_list = list(kwic.generate_kwic(test_file_path))

            self.assertEqual(kwic_list, expected_kwic)

if __name__ == "__main__":
    unittest.main()
