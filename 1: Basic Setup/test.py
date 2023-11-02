#!/usr/bin/env python3
"""NXT-Python tutorial: find the brick."""

import nxt.locator
import time


MIDDLE_C = 261
MIDDLE_A = 440

def playTone(brick,note,duration):
      b.play_tone(note, duration)
      time.sleep(duration / 1000)

# Find a brick.
with nxt.locator.find() as b:
    # Once found, print its name.
    print("Found brick:", b.get_device_info()[0])
    # And play a recognizable note. Frequency(Hz), duration (ms)

    playTone(b,MIDDLE_C, 250)
    playTone(b,MIDDLE_A, 250)
    playTone(b,MIDDLE_C, 250)
    playTone(b,MIDDLE_A, 250)
    playTone(b,MIDDLE_C, 250)
    playTone(b,MIDDLE_A, 250)
 

