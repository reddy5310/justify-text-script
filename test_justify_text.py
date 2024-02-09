import unittest
from justify_text import justify_text  # Make sure to adjust import path as needed

class TestJustifyText(unittest.TestCase):
    def test_single_line(self):
        paragraph = "This is a test."
        page_width = 20
        expected = ["This is a test.    "]  # Adjust expected result based on implementation
        self.assertEqual(justify_text(paragraph, page_width), expected)

    def test_multiple_lines(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20
        expected = [
            "This  is  a  sample",  # Expected results might need adjustments
            "text  but  a      ",
            "complicated problem",
            "to be solved, so we",
            "are  adding  more  ",
            "text to see that it",
            "actually works.    "
        ]
        self.assertEqual(justify_text(paragraph, page_width), expected)

    def test_empty_paragraph(self):
        paragraph = ""
        page_width = 20
        expected = [""]
        self.assertEqual(justify_text(paragraph, page_width), expected)

    def test_page_width_too_small(self):
        paragraph = "This is a test."
        page_width = 5
        # Assuming function handles small page width by not breaking words and simply overflowing the width
        expected = ["This is a test."]
        self.assertEqual(justify_text(paragraph, page_width), expected)

# Add more test cases to test

if __name__ == '__main__':
    unittest.main()
