#!/usr/bin/env python3
"""NXT-Python tutorial: find the brick."""

import nxt.locator
import time


MIDDLE_C = 261
MIDDLE_A = 440

# And play a recognizable note. Frequency(Hz), duration (ms)
# brick:object
# note:note to play Hz
# dutation in ms
def playTone(brick:object,note:int,duration:int):
      brick.play_tone(note, duration)
      time.sleep(duration / 1000)


def main():
      # Find a brick.
      with nxt.locator.find() as b:
      # Once found, print its name.
            print("Found brick:", b.get_device_info()[0])
            

            playTone(b,MIDDLE_C, 250)
            playTone(b,MIDDLE_A, 250)
            playTone(b,MIDDLE_C, 250)
            playTone(b,MIDDLE_A, 250)
            playTone(b,MIDDLE_C, 250)
            playTone(b,MIDDLE_A, 250)
 
if __name__ == "__main__":
    main()
