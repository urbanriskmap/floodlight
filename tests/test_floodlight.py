import unittest
from unittest.mock import patch
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

# Before:
# Mock client (self.client.put_pixels)
# Tests:
    # Catches bad fadecandy connection
    # Catches bad report count, returns -1
    # Check _send_sequence waits if > timing > 0
    # Check main loop

import floodlight

config = json.load(open('config.json'))

class TestFloodlight(unittest.TestCase):

    def test_init_error(self):
        """Catches error with Fadecandy connection"""
        try:
            config['fadecandy']['long_connection'] = False
            floodlight.FloodLight(config)
        except Exception as e:
            self.assertEqual('Could not connect to Fadecandy server at %s' % config['fadecandy']['server'], str(e))

    @patch('_opc.Client.can_connect')
    def test_init(self, mock_can_connect):
        """Can initialize instance of FloodLight class"""
        # disconnect
        mock_can_connect.return_value = True
        config['fadecandy']['long_connection'] = False
        self.assertIsInstance(floodlight.FloodLight(config), floodlight.FloodLight)

    @patch('_opc.Client.can_connect')
    def test_get_report_count_error(self, mock_can_connect):
        mock_can_connect.return_value = True
        config['fadecandy']['long_connection'] = False
        config['cognicity']['reports_endpoint'] = 'http://localhost'
        count = floodlight.FloodLight(config)._get_report_count()
        self.assertEqual(count, -1)

        
    """def test_client(self, mock_api_call):
        mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'key':'value'}))
        fl._send_sequence([{pattern:[(1,2,3)],timing:0}])"""



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
