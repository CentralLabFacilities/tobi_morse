import time
from pymorse import Morse

with Morse() as morse:
    motion = morse.human.human_motion
    x = 2
    while True:
        x = -x
        y = 0
        print("Moving to %s..." % ([x, y],))
        motion.publish({"x":x, "y":y, 'z':0, 'tolerance':0.3, 'speed':1})
        time.sleep(0.5)