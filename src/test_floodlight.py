import unittest, sys

import floodlight

NUM_LED = 48
BLUE = (49, 170, 222)
RED = (240, 80, 34)
GREEN = (0, 255, 0)

class TestSystemFunctions(unittest.TestCase):

    def test_system_error(self):
        pixels = [(0,0,0)] * NUM_LED
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
