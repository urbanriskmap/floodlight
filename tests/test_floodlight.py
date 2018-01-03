import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys
import os
import json
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import floodlight
import _sequence
import _config

config = _config.load_config('config.json')

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

        # Mock the OPC can_connect function
        mock_can_connect.return_value = True
        # Check it is the right object
        self.assertIsInstance(floodlight.FloodLight(config), floodlight.FloodLight)


    @patch('_opc.Client.can_connect')
    def test_get_report_count_error(self, mock_can_connect):
        """Can catch errors with CogniCity endpoint"""

        # Mock the OPC can_connect function
        mock_can_connect.return_value = True
        # Set the config endpoint to junk
        config['cognicity']['reports_endpoint'] = 'http://localhost'
        # Get the error count
        count = floodlight.FloodLight(config)._get_report_count()
        self.assertEqual(count, -1)



    @patch('floodlight.requests.get')
    @patch('_opc.Client.can_connect')
    def test_get_report_count(self, mock_can_connect, mock_requests_get):
        """Returns count of GeoJSON object"""

        # Mock the OPC can_connect function
        mock_can_connect.return_value = True
        # Mock the requests object
        mock_requests_get.return_value = MagicMock(status_code=200, json=lambda : json.loads(json.dumps({'result':{'features':[0,1,2]}})))
        # Initialize the class
        count = floodlight.FloodLight(config)._get_report_count()
        # Test
        self.assertEqual(count, 3)

    @patch('floodlight.time.sleep', return_value=None)
    @patch('_opc.Client.put_pixels', return_value=None)
    @patch('_opc.Client.can_connect')
    def test_send_sequence(self, mock_can_connect, mock_put_pixels, mock_time_sleep):
        """Test send sequence method"""

        # Mock the OPC can_connect function
        mock_can_connect.return_value = True

        # Execute the send sequence method
        floodlight.FloodLight(config)._send_sequence([{'pattern':[(1,2,3)],'timing':10}])

        # Test that put pixels called with expected value
        mock_put_pixels.assert_called_with([(1,2,3)])

        # Check that sleep value called as expected
        mock_time_sleep.assert_called_with(10)

    @patch('floodlight.time.sleep', return_value=None, side_effect=InterruptedError)
    @patch('_opc.Client.put_pixels', return_value=None)
    @patch('_opc.Client.can_connect')
    @patch('floodlight.FloodLight._send_sequence', return_value=None)
    @patch('floodlight.FloodLight._get_report_count')
    def test_start(self, mock_get_report_count, mock_send_sequence, mock_can_connect, mock_put_pixels, mock_time_sleep):
        """Test send sequence method"""

        mock_get_report_count.return_value = 2

        # Mock the OPC can_connect function
        mock_can_connect.return_value = True

        # Execute the send sequence method
        try:
            floodlight.FloodLight(config).start()
        except InterruptedError:

            # Construct the expected sequence
            sequence = _sequence.Sequence(config).build(0, 2)

            # Test that put pixels called with expected value
            mock_send_sequence.assert_called_with(sequence)

            # Check that sleep value called as expected
            mock_time_sleep.assert_called_with(60)

if __name__ == '__main__':
    unittest.main()
