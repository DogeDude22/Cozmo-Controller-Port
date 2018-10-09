"""Simple example showing how to get gamepad events."""

from __future__ import print_function


from inputs import get_gamepad


def main():
    Y = 0
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.code, event.state)
            if event.code =="BTN_NORTH":
                    print("Y Has been pressed")
                    Y = Y + 1
            if event.state == "0":
                print ("Y was Realeased")
                Y = Y - 1


if __name__ == "__main__":
    main()




