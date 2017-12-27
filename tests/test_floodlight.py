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
    # Catches bad fadecandy connection
    # Catches bad report count, returns -1
    # Check _send_sequence waits if > timing > 0
    # Check main loop

import floodlight

config = json.load(open('config.json'))
# Use short connection for tests
config['fadecandy']['long_connection'] = False

class TestFloodlight(unittest.TestCase):

    # This method will be used by the mock to replace requests.get
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                print('yippeeeeeeeee')
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                yield self.json_data

        if args[0] == 'http://someurl.com/test.json':
            yield MockResponse({"key1": "value1"}, 200)
        elif args[0] == 'http://someotherurl.com/anothertest.json':
            yield MockResponse({"key2": "value2"}, 200)
        yield MockResponse(None, 404)

    def test_init_error(self):
        """Catches error with Fadecandy connection"""
        try:
            floodlight.FloodLight(config)
        except Exception as e:
            self.assertEqual('Could not connect to Fadecandy server at %s' % config['fadecandy']['server'], str(e))

    @patch('_opc.Client.can_connect')
    def test_init(self, mock_can_connect):
        """Can initialize instance of FloodLight class"""
        # disconnect
        mock_can_connect.return_value = True
        self.assertIsInstance(floodlight.FloodLight(config), floodlight.FloodLight)

    @patch('_opc.Client.can_connect')
    def test_get_report_count_error(self, mock_can_connect):
        mock_can_connect.return_value = True
        config['cognicity']['reports_endpoint'] = 'http://localhost'
        count = floodlight.FloodLight(config)._get_report_count()
        self.assertEqual(count, -1)


    @patch('_opc.Client.can_connect')
    def test_get_report_count(self, mock_can_connect):
        with patch('requests.get') as mock_request:
            mock_request.return_value = MagicMock(status_code=200, json=lambda : json.loads(json.dumps({'result':{'features':[0,1,2]}})))
            config['cognicity']['reports_endpoint'] = 'http://localhost'
            count = floodlight.FloodLight(config)._get_report_count()
            self.assertEqual(count, 3)

        #mock_can_connect.return_value = True
        #mocked_requests_get.return_value = MagicMock(status_code=200, response=json.dumps({'spam':{'features':[0,1]}}))





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
