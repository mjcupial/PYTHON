import unittest
from element import spin_words

class ActivityTests(unittest.TestCase):
    def test_single_word(self):
        """Single word"""
        self.assertEqual(
            spin_words("Welcome"),
            "emocleW"
        )
        self.assertEqual(
            spin_words("Maciej"),
            "jeicaM"
        )
    def test_multiple_words(self):
        """Multiple words"""
        self.assertEqual(
            spin_words("Hey fellow warriors"),
            "Hey wollef sroirraw"
        )
        self.assertEqual(
            spin_words("This sentence is a sentence"),
            "This ecnetnes is a ecnetnes"
        )

if __name__ == '__main__':
    unittest.main()