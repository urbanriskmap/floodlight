import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import _config
import _pattern

config = _config.load_config('config.json')
pt = _pattern.Pattern(config)

class TestPattern(unittest.TestCase):

    def test_error(self):
        pixels = [(0,0,0)] * config['fadecandy']['led_strip_length']
        pixels[0] =  config['colors']['red']
        self.assertEqual(pt.error(), pixels)

    def test_system_online(self):
        pixels = [(0,0,0)] * config['fadecandy']['led_strip_length']
        pixels[0] =  config['colors']['green']
        self.assertEqual(pt.online(), pixels)

    def test_system_new_report(self):
        pixels = [config['colors']['blue']] * config['fadecandy']['led_strip_length']

        self.assertEqual(pt.new_report(), pixels)

    def test_system_flood(self):
        pixels = [(0,0,0)] * config['fadecandy']['led_strip_length']
        pixels[0] = config['colors']['blue']
        self.assertEqual(pt.flood(1), pixels)


if __name__ == '__main__':
    unittest.main()
