# -*- coding: utf-8 -*-
import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import floodlight

config = json.load(open('config.json'))

fl = floodlight.FloodLight(config)

    """ Sample test
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """


if __name__ == '__main__':
    unittest.main()
