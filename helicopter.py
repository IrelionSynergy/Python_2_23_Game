from utils import random_point
from map import CELL_TYPES

class Helicopter:
    def __init__(self, weidth, higth):
        rc = random_point(weidth, higth)
        rx, ry = rc[0], rc[1]
        self.higth = higth
        self.weidth = weidth
        self.x = rx
        self.y = ry
        self.tank = 0
        self.maxtank = 1
        self.score = 0

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.higth and ny < self.weidth):
            self.x, self.y = nx, ny

    def print_stats(self):
        print(f'{CELL_TYPES.get('tank')}: {self.tank}/{self.maxtank} | {CELL_TYPES.get('score')} {self.score}')