from utils import random_point
from map import CELL_TYPES
from map import UPGRADE_COST
import time
import os

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
        self.lives = 200

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
        print(f'{CELL_TYPES.get('tank')}: {self.tank}/{self.maxtank} | {CELL_TYPES.get('score')} {self.score} | {CELL_TYPES.get('upgrade')} cost: {UPGRADE_COST * self.maxtank}')
        print(f'{CELL_TYPES.get('lives')}: {self.lives}')

    def game_over(self):
        os.system('cls')
        print('GAME OVER')
        time.sleep(3)
        exit(0)

    def export_data(self):
        return {
            'score': self.score,
            'lives': self.lives,
            'x': self.get_x(),
            'y': self.get_y(),
            'tank': self.tank,
            'maxtank': self.maxtank
        }
    
    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.maxtank = data['maxtank'] or 1
        self.score = data['score'] or 0
        self.lives = data['lives'] or 3