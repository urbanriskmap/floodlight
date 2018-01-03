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

LOG_FORMAT = ('%(asctime)s %(filename)s '
              '(function: %(funcName)s line: %(lineno)s) Message: %(message)s')

logger = logging.getLogger(__name__)
config_file = os.path.dirname(__file__) + '/../config.json'


def main():
    """Run floodlight"""
    # Load config
    config = _config.load_config(config_file)
    # Create log file
    logging.basicConfig(filename=config['logfile']['path'],
                        level=logging.DEBUG,
                        format=LOG_FORMAT)

    # Create floodlight instance
    fl = floodlight.FloodLight(config)
    # Start process, catching KeyboardInterrupts
    try:
        fl.start()
    except KeyboardInterrupt:
        logger.info("Exit called by user (KeyboardInterrupt), will now exit.")
        sys.exit(0)


main()
