FloodLight
==========
[![Build Status](https://travis-ci.org/urbanriskmap/floodlight.svg?branch=master)](https://travis-ci.org/urbanriskmap/floodlight)

Interface to Fadecandy LED strip to display CogniCity flood reports

### Requirements
- Python (version?)
- Access to a Fadecandy server
- Reports from a CogniCity server in GeoJSON format

### Install

```sh
pip install -r  requirements.txt
```

### Run

```
python floodlight
```

### Configuration Parameters
`config.json`

- Fadecandy:
  * `server` - address and port of fadecandy server (e.g. localhost:7890)
  * `long_connection` - true/false fadecandy connection type
  * `led_strip_length` - number of LEDs in display
- CogniCity:
  * `reports_endpoint` - server endpoint for flood reports in GeoJSON format (e.g. data.petabencana.id/reports?format=geojson)
  * `poll_interval` - how long between requests for new reports (seconds)
- Colors:
  * Custom (rgb) definitions for red, green and blue
  - for example; ``"red": [240, 80, 34]``

### Software Modules
- `__main__.py` - Called when running from commandline, loads config and starts process
- `floodlight.py` - Gets CogniCity report count and sends instructions to Fadecandy server
- `_pattern.py` - Lighting patterns for Fadecandy LED strip
- `_sequence.py` - Group lighting patterns to animate LED strip through time


### Testing
Code should conform to Python PEP8 style, which can be checked by running:
```sh
pycodestyle floodlight/floodlight.py floodlight/_pattern.py floodlight/_sequence.py
```

Unit tests are written using Python unittest and can be run by doing:
```sh
python -W ignore -m unittest discover tests
```
The `-W` flag is used to ignore warning messages that come from the socket library used by fadecandy `_opc.py`

### License
