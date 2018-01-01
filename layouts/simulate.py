import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import _config
import _sequence
import floodlight

config = _config.load_config('config.json')
fl = floodlight.FloodLight(config)
sq = _sequence.Sequence(config)

#fl._send_sequence(sq.online())

sequence = sq.build(10, 12)

fl._send_sequence(sequence)
#fl.start()
