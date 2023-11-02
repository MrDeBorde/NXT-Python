#!/usr/bin/python3
"""Boiler Plate code to organise your code """
# import modules
import time
import nxt.locator
# Need to import generic sensors for auto-detection to work.
import nxt.sensor.generic

# define functions to do tasks
def get_distance(sensor):
    return sensor.get_sample()

#main function for the operation to mimic your flow chart
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

# run the main function on start up
# code will not run with out this
if __name__ == "__main__":
    main()