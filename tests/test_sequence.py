import unittest
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import _config
import _sequence
import _pattern

config = _config.load_config('config.json')
pt = _pattern.Pattern(config)
sq = _sequence.Sequence(config)

class TestSequence(unittest.TestCase):

    def test_build(self):
        """Test Sequence builder"""

        self.assertEqual(sq.build(0, 0), sq.online())
        self.assertEqual(sq.build(0, 1), sq.rainfall(1))
        self.assertEqual(sq.build(1, 1), sq.flood(1))
        self.assertEqual(sq.build(-1, -1), sq.error())

if __name__ == '__main__':
    unittest.main()
