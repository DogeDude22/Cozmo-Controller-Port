from __future__ import print_function
from inputs import get_gamepad

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps



def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.code,event.state)
            if event.code==

if __name__ == "__main__":
    main()


def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    
cozmo.run_program(cozmo_program)
