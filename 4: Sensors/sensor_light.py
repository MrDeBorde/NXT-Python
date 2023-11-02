#!/usr/bin/python3
"""NXT-Python boilerplate for light sensor."""
import time

import nxt.locator
import nxt.sensor
import nxt.sensor.generic

def get_touch(sensor):
    return sensor.get_sample()

def main():

    with nxt.locator.find() as b:
        # Get the sensor connected to port 1, not a digital sensor, must give the sensor
        # class.
        mysensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Light)
        # Read the sensor in a loop (until interrupted).
        print("Use Ctrl-C to interrupt")
        while True:
            value = get_touch(mysensor)
            print(value)
            time.sleep(0.5)

if __name__ == "__main__":
    main()