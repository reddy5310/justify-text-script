import unittest
from justify_text import justify_text  # Ensure to match the actual import path

class TestJustifyText(unittest.TestCase):
    
    def test_basic_justification(self):
        paragraph = "This is a test."
        page_width = 14
        expected = ["This is a test."]
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected)
        
    def test_full_justification(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20
        expected = [
            "This  is  a sample",
            "text  but a      ",
            "complicated      ",
            "problem to be    ",
            "solved, so we are",
            "adding more text ",
            "to see that it   ",
            "actually  works. "
        ]
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected)

    def test_single_word_line(self):
        paragraph = "Word"
        page_width = 10
        expected = ["Word      "]
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected)

    def test_paragraph_with_long_word(self):
        paragraph = "This wordiswaytoolongforasingleline"
        page_width = 10
        expected = ["This      ", "wordiswayt", "oolongfora", "singleline"]
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected)

    def test_empty_paragraph(self):
        paragraph = ""
        page_width = 20
        expected = []
        result = justify_text(paragraph, page_width)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
