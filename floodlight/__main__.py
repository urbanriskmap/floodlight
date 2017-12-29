"""
FloodLight - Fadecandy LED interface for CogniCity Reports

Tomas Holderness, MIT 2017

v0.0.1
"""
__author__ = "Tomas Holderness"
__created__ = "2017-12-21"
__version__ = "0.0.1"
__copyright__ = "Copyright 2017 MIT Urban Risk Lab"
__license__ = "GPLv3"
__email__ = "tomash@mit.edu"
__status__ = "Development"
__url__ = "https://github.com/urbanriskmap/floodlight"

import _config
import floodlight

# TODO
# - rainfall light style for new flood report
def main():
    config = _config.load_config('config.json')
    # Create floodlight instance
    fl = floodlight.FloodLight(config)
    # Start process
    fl.start()

main()
