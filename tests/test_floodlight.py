import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

# Before:
# Mock client (self.client.put_pixels)
# Tests:
    # Check _send_sequence waits if > timing > 0
    # Check main loop

import floodlight

config = json.load(open('config.json'))
# Use short connection for tests
config['fadecandy']['long_connection'] = False

class TestFloodlight(unittest.TestCase):

    def test_init_error(self):
        """Catches error with Fadecandy connection"""

        try:
            floodlight.FloodLight(config)
        except Exception as e:
            self.assertEqual('Could not connect to Fadecandy server at %s' % config['fadecandy']['server'], str(e))

    @patch('_opc.Client.can_connect')
    def test_init(self, mock_can_connect):
        """Can initialize instance of FloodLight class"""

        mock_can_connect.return_value = True
        self.assertIsInstance(floodlight.FloodLight(config), floodlight.FloodLight)

    @patch('_opc.Client.can_connect')
    def test_get_report_count_error(self, mock_can_connect):
        """Can catch errors with CogniCity endpoint"""

        mock_can_connect.return_value = True
        config['cognicity']['reports_endpoint'] = 'http://localhost'
        count = floodlight.FloodLight(config)._get_report_count()
        self.assertEqual(count, -1)


    @patch('floodlight.requests.get')
    @patch('_opc.Client.can_connect')
    def test_get_report_count(self, mock_can_connect, mock_requests_get):
        """Returns count of GeoJSON object"""

        # Mock the requests object
        mock_requests_get.return_value = MagicMock(status_code=200, json=lambda : json.loads(json.dumps({'result':{'features':[0,1,2]}})))
        # Set the config endpoint to junk
        config['cognicity']['reports_endpoint'] = 'http://localhost'
        # Initialize the class
        count = floodlight.FloodLight(config)._get_report_count()
        # Test
        self.assertEqual(count, 3)

"""Sample test
def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
        s.split(2)
"""


if __name__ == '__main__':
    unittest.main()
