"""FloodLight - Fadecandy LED interface for CogniCity Reports"""

# External Dependencies
import time
import requests
import logging

# Submodules
import _opc
import _sequence

logger = logging.getLogger(__name__)

class FloodLight:
    """Main class for FloodLight module"""

    def __init__(self, config):
        """Accepts a configuration object returns a FloodLight object"""
        self.config = config
        self.sequence = _sequence.Sequence(self.config)
        self.client = _opc.Client(self.config['fadecandy']['server'],
                                  self.config['fadecandy']['long_connection'])

        # Check fadecandy connection
        connection = self.client.can_connect()
        if (connection is False):
            message = ('Could not connect to Fadecandy server at %s' %
                       self.config['fadecandy']['server'])
            logger.error(message)
            raise RuntimeError(message)

    def _get_report_count(self):
        """Get the number of flood reports in the past hour"""
        count = -1
        try:
            r = requests.get(self.config['cognicity']['reports_endpoint'])
            if (r.status_code == 200):
                count = (len(r.json()['result']['features']))
        except Exception as e:
            message = "Error getting report count: " + str(e)
            logger.error(message)
        return (count)

    def _send_sequence(self, sequence):
        """Accepts array of patterns and timings, sends to fadecandy server"""
        for item in sequence:
            self.client.put_pixels(item['pattern'])
            if item['timing'] > 0:
                time.sleep(item['timing'])

    def start(self):
        """Polls CogniCity endpoint and sends sequences to fadecandy"""
        # Store the last count
        last_count = 0

        # Reset the lights at first run
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        self.client.put_pixels(pixels)

        # Main loop
        while True:
            # Get the latest report count, and send a new light sequence
            new_count = self._get_report_count()
            sequence = self.sequence.build(last_count, new_count)
            self._send_sequence(sequence)

            # update the count an add a print a message before the next update
            last_count = new_count
            logger.info('Next update in %s seconds...' %
                    self.config['cognicity']['poll_interval'])
            time.sleep(self.config['cognicity']['poll_interval'])
