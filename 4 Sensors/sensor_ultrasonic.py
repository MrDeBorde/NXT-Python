#!/usr/bin/python3
"""Boiler plage for untrasonic."""
import time

import nxt.locator
import nxt.sensor

# Need to import generic sensors for auto-detection to work.
# auto detection only works on digital sensors
# Ultrasonic being one of them
import nxt.sensor.generic

def get_distance(sensor):
    return sensor.get_sample()

def main():
    with nxt.locator.find() as b:
    # Find the sensor connected to port 4.
        mysensor = b.get_sensor(nxt.sensor.Port.S4)
        # Read the sensor in a loop (until interrupted).
        print("Use Ctrl-C to interrupt")
        while True:
            distance_cm = get_distance(mysensor)
            print(distance_cm)
            time.sleep(0.5) 

if __name__ == "__main__":
    main()