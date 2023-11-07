#!/usr/bin/python3
"""
Working out how to record the starting poition of a motor
do some rotations then return it back to start positon
"""
import nxt.locator
import nxt.motor

# rotation is tacho_untis
def turn_motor(motor,speed,rotation):
    motor.turn(speed, rotation)

def main():
    with nxt.locator.find() as b:
        # Get the motor connected to the port A.
        motor_1 = b.get_motor(nxt.motor.Port.A)

        #reset the position of the motor, variable for tacho position.
        motor_1.reset_position(True)
        position=int(motor_1.get_tacho().block_tacho_count)

        # example to move motor with run and a limit of 200 units
        limit = int(200)
        while position < limit:
            motor_1.run(100,True)
            position=int(motor_1.get_tacho().block_tacho_count)
            print("position",position)
        #motor_1.brake() can cause a kickback ? # brake to stop motor
        motor_1.idle() 
        # disconnects motor, turns OFF will roll if not under load
        # advided to do this after a .run()
       
       
        turn_motor(motor_1,100,200) 
        """ does the same really in outcome, but not way, 
        motor.run and motor.turn different
        motor.run can be interrupted by sensors (non blockikg)
        motor.turn has to comlete the code (blocking all other)
        """

       
        """ to return back to sart, reverse direction
        until position is 0"""

        while position > 0:
            motor_1.run(-100,True)
            position=int(motor_1.get_tacho().block_tacho_count)
            print("position",position)
        #motor_1.brake() #stop motor, but still ON
        motor_1.idle() 

if __name__ == "__main__":
    main()