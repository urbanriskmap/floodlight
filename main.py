#!/usr/bin/env python

# cognicity-led - LED interface for CogniCity reports
# 2017-12-21

import opc, time, requests # imports

# Number of LEDs
NUM_LED = 48
# API for reports
COGNICITY_ENDPOINT = 'https://data-dev.petabencana.id/reports?geoformat=geojson'

# Color definitations
BLUE = (49, 170, 222)
RED = (240, 80, 34)
GREEN = (0, 255, 0)

# Poll interval
INTERVAL = 60

# Create an LED client
client = opc.Client('localhost:7890')

# Store the number of reports
last_count = 0

# Setup the lights
pixels = [ BLUE ] * NUM_LED

# Turn off the lights
client.put_pixels(pixels)

def get_report_count( url ):
    """Get the number of flood reports in the past hour"""
    count = -1
    try:
        r = requests.get(url)
        if (r.status_code == 200):
            count = (len(r.json()['result']['features']))
    except Exception as e:
        print ("Error getting report count: " + str(e))

    return (count)

def system_error():
    """Set the first LED to red"""
    pixels = [ (0,0,0) ] * NUM_LED
    pixels[0] = RED
    return (pixels)

def system_online():
    """Set the first LED to green"""
    pixels = [ (0,0,0) ] * NUM_LED
    pixels[0] = GREEN
    return (pixels)

def system_new_report ():
    """Set all LEDs to blue for new report alert"""
    return ([ BLUE ] * NUM_LED)

def system_flood(num_reports):
    """Set LEDs to number of reports"""
    pixels = [ (0,0,0) ] * NUM_LED
    for i in range(0, num_reports):
        pixels[i] = BLUE
    return (pixels)

# Start a loop to periodically update the lights
while True:
    # Get current reports from server
    latest_count = get_report_count(COGNICITY_ENDPOINT)
    client.put_pixels(system_error())
    time.sleep(0.1)
    if latest_count == 0:
        client.put_pixels(system_online())
    elif latest_count > last_count:
        client.put_pixels(system_new_report())
        time.sleep(2)
        client.put_pixels(system_flood(latest_count))
    else:
        client.put_pixels(system_flood(latest_count))
    last_count = latest_count
    time.sleep(INTERVAL)
