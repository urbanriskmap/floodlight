#!/usr/bin/env python

# cognicity-led - LED interface for CogniCity reports
# 2017-12-21

import opc, time, requests # imports
NUM_LED = 30

# Create an LED client
client = opc.Client('localhost:7890')

# Store the number of reports
num_reports = 0

# Setup the lights
pixels = [ (0,0,0) ] * NUM_LED

# Turn off the lights
client.put_pixels(pixels)

# Loop
while True:
    # Get current reports from server
    r = requests.get('https://data-dev.petabencana.id/reports?geoformat=geojson')
    # Make LEDs red if theres a problem
    if (r.status_code != 200):
        for i in range(0, NUM_LED):
            pixels[i] = (255,0,0)
    else:
        # Get the latest number of reports
        new_num = len(r.json()['result']['features'])
        # If new report then flash the light
        if (new_num > 0):
            if (new_num > num_reports):
                client.put_pixels([(0,0,255)] * NUM_LED)
                time.sleep(0.5)
            # Set the lights per the number of reports
            for i in range(0, new_num):
                pixels[i] = (0,0,255)
        # No new reports so just set one light as green
        else:
            pixels[0] = (0,255,0)
        # Update the report count
        num_reports = new_num
    # Update the lights
    client.put_pixels(pixels)
    # Wait 60s before the next update
    time.sleep(60)
