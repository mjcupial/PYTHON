import unittest
from example import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, becaFAILuse my body is a temple"
        )
    def test_eat_unhealthy(self):
        """eat should indicate you've given up for eating unhealthy"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO"
        )

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3), "Ugh I overslept.  I didn't mean to nap for 3 hours!"
        )

if __name__ == '__main__':
    unittest.main()