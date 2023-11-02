#!/usr/bin/python3
"""NXT-Python tutorial: turn a motor."""
"""From NXT-Python Tutorials"""
import nxt.locator
import nxt.motor


def turn_motor(motor,speed,rotation):
    motor.turn(speed, rotation)

def main():
    with nxt.locator.find() as b:
        # Get the motor connected to the port A.
        motor_1 = b.get_motor(nxt.motor.Port.A)

        turn_motor(motor_1,25,360)

        turn_motor(motor_1,-50,360)

if __name__ == "__main__":
    main()