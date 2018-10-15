"""Simple example showing how to get gamepad events."""

from __future__ import print_function
from inputs import get_gamepad
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def main(robot: cozmo.robot.Robot):
    while 1: 
        events = get_gamepad() 
        for event in events:  
            print(event.code, event.state)
            if event.code == "ABS_RZ" and event.state > 150:
                robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
            if event.code == "ABS_Z" and event.state > 150:
               robot.drive_straight(distance_mm(-150), speed_mmps(50)).wait_for_completed() 
            if event.code == "ABS_HAT0Y" and event.state == -1:
                robot.move_lift(5)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                robot.move_lift(-5)
                
 


cozmo.run_program(main, use_viewer=True, force_viewer_on_top=True)

if __name__ == "__main__": 
      main() 
