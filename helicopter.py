from utils import random_point

class Helicopter:
    def __init__(self, weidth, higth):
        rc = random_point(weidth, higth)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry