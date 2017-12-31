import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import _config
import _sequence

config = _config.load_config('config.json')
sq = _sequence.Sequence(config)

class TestSequence(unittest.TestCase):

    def test_build(self):
        """Test Sequence builder"""

        self.assertEqual(sq.build(0, 0), sq.online())
        self.assertEqual(sq.build(0, 1), sq.new_report(0, 1))
        self.assertEqual(sq.build(1, 1), sq.flood(1))
        self.assertEqual(sq.build(-1, -1), sq.error())

if __name__ == '__main__':
    unittest.main()
