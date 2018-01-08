"""
FloodLight - Fadecandy LED interface for CogniCity Reports

Tomas Holderness, MIT 2017

v0.0.4
"""
__author__ = "Tomas Holderness"
__created__ = "2017-12-21"
__version__ = "0.0.4"
__copyright__ = "Copyright 2017 MIT Urban Risk Lab"
__license__ = "GPLv3"
__email__ = "tomash@mit.edu"
__status__ = "Development"
__url__ = "https://github.com/urbanriskmap/floodlight"

import os
import sys
import logging
import _config
import floodlight

# Load config
config_file = os.path.dirname(__file__) + '/../config.json'
config = _config.load_config(config_file)

# Create log file
log_format = ('%(asctime)s %(filename)s '
              '(function: %(funcName)s, line: %(lineno)s) '
              'Message: %(message)s')
logging.basicConfig(filename=config['logfile']['path'],
                    level=config['logfile']['level'],
                    format=log_format)
# Silence the requests module
logging.getLogger("requests").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    """Run floodlight"""
    # Create floodlight instance
    fl = floodlight.FloodLight(config)
    # Start process, catching KeyboardInterrupts
    try:
        fl.start()
    except KeyboardInterrupt:
        logger.info("Exit called by user (KeyboardInterrupt), will now exit.")
        sys.exit(0)


main()
