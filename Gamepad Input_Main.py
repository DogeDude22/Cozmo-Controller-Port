"""Simple example showing how to get gamepad events."""

from __future__ import print_function
from inputs import get_gamepad
import cozmo


def main(robot: cozmo.robot.Robot):
 while 1: 
    events = get_gamepad() 
    for event in events: 
        print(event.code,event.state) 
        if event.code == "ABS_RZ":
               robot.say_text("I am moving").wait_for_completed()
 

cozmo.run_program(main)

if __name__ == "__main__": 
      main() 


 
  









