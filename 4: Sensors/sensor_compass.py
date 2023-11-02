#!/usr/bin/python3
"""NXT-Python boilerplate for compass sensor."""
import time

import nxt.locator
import nxt.sensor
import nxt.sensor.generic
import nxt.sensor.hitechnic
# The Compass is in a different module to import.

def get_direction(sensor):
    return sensor.get_heading()

def main():

    with nxt.locator.find() as b:
        # Get the sensor connected to port 1, not a digital sensor, must give the sensor
        # class.
        mysensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.hitechnic.Compass)
        # Read the sensor in a loop (until interrupted).
        print("Use Ctrl-C to interrupt")
        while True:
            value = get_direction(mysensor)
            print(value)
            time.sleep(0.5)

if __name__ == "__main__":
    main()