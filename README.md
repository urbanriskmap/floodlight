FloodLight
==========
[![Build Status](https://travis-ci.org/urbanriskmap/floodlight.svg?branch=master)](https://travis-ci.org/urbanriskmap/floodlight)

Interface to Fadecandy LED strip to display CogniCity flood reports

### Requirements
- Python (version?)
- Access to Fadecandy server
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
  * `led_strip_length` - number of LEDs in display
- CogniCity:
  * `reports_endpoint` - server endpoint for flood reports in GeoJSON format (e.g. data.petabencana.id/reports?format=geojson)
  * `poll_interval` - how long between requests for new reports (seconds)
- Colors:
  * Custom (rgb) definitions for red, green and blue
  - for example; ``"red": [240, 80, 34]``

### Software Modules
