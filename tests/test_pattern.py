import unittest
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import pattern
config = json.load(open('config.json'))

pt = pattern.Pattern(config)

class TestPatterns(unittest.TestCase, config):

    def test_error(self):
        pixels = [(0,0,0)] * config
        pixels[0] =  RED
        self.assertEqual(floodlight.system_error(), pixels)

    def test_system_online(self):
        pixels = [(0,0,0)] * NUM_LED
        pixels[0] =  GREEN
        self.assertEqual(floodlight.system_online(), pixels)

    def test_system_new_report(self):
        pixels = [BLUE] * NUM_LED
        self.assertEqual(floodlight.system_new_report(), pixels)

    def test_system_flood(self):
        pixels = [(0,0,0)] * NUM_LED
        pixels[0] = BLUE
        self.assertEqual(floodlight.system_flood(1), pixels)
