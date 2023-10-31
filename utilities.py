#!/usr/bin/env python3

import nxt.locator
import usb.core
import time
import itertools, sys

spinner = itertools.cycle(['-', '/', '|', '\\'])

"""
      function to locate the bricks by name
      and return the brick object
"""

def locate_brick(brick):
      # find the bricks connected to the computer
      print ("Locating brick...",brick)
      trys = 0
      while True:
            try:
                  #change trys if you need to
                  if trys == 20:
                        break
                  # simple spinner for progress
                  sys.stdout.write(next(spinner))   # write the next character
                  sys.stdout.flush()                # flush stdout buffer (actual character display)
                  sys.stdout.write('\b')            # erase the last written char
                  return nxt.locator.find(name=brick) 
            except nxt.locator.BrickNotFoundError:
                  #print ("  No Brick Found")
                  trys = trys+1
            except usb.core.USBError:
                  #print("  Searching for",brick)
                  trys = trys+1
          