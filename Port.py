
from __future__ import print_function
from inputs import get_gamepad
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps



def main(robot: cozmo.robot.Robot):
 while 1: 
    events = get_gamepad() 
    for event in events: 
        print(event.code,event.state) 
        if event.code == "ABS_RZ":
               robot.say_text("I am moving").wait_for_completed()
               robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        if event.code == "ABS_Z": 
               robot.say_text("I am moving backward").wait_for_completed()
               robot.drive_straight(distance_mm(-150), speed_mmps(50)).wait_for_completed()

               
               

            


cozmo.run_program(main)

if __name__ == "__main__": 
      main() 
