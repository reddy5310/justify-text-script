import unittest
from justify_text import justify_text

class TestJustifyText(unittest.TestCase):
    def test_justify_text_simple(self):
        paragraph = "This is a test."
        page_width = 10
        expected_output = ["This is a", "test."]
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
