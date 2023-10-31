#!/usr/bin/env python3
"""NXT-Python : 2 bricks test."""
"""   
      Test program to use more than one named brick
      as long as thecan be both connected
      and you know the names.
      Will work for just one too.
      Displays progress... could be more stylish
"""
from utilities import *

import time


                  
# Just a demo function to test on each brick                   
def playTone(BRICK):
      try:
            BRICK.play_tone(400, 250)
            time.sleep(250 / 1000)
            BRICK.play_tone(300, 250)
            time.sleep(250 / 1000)
      except AttributeError:
            print("Error playing sound ")


#the main function
def main():
      print ("Main function")

      # these were the names of the bricks I tes ted.. you can renal and use your own
      LOL = locate_brick("LOL")
      NXT = locate_brick("NXT")

      #test to see if the bricks have been found, both (or one_) needed for functionality.
      # Exits if not available
      if LOL is  None or NXT is  None:
            print ("Not all bricks not found, check power, connection.. or try again")
            exit()

      #Now the bricks are addressable and can use methods
      # for each one, or create other functions to do things like motors and sensors
      print("Bricks identified... lets Go!!!")

      print("Press Enter key to continue...")
      input()
       
      #print(LOL)
      playTone(LOL)

      #print(NXT)
      playTone(NXT)

      # close the connections... 
      # good practice to to close connections before ending
      
      LOL.close()
      NXT.close()
     
if __name__ == "__main__":
    main()