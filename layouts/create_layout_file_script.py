import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../floodlight')))

import _config

config = _config.load_config('config.json')

output = []
for i in range(0, config['fadecandy']['led_strip_length']):
    # layout file takes coordinates "x", "y", "z"
    output.append({"point": [0, i, 0]})
    #print ('{"point": [0, i, 0]}')

print(json.dumps(output))
