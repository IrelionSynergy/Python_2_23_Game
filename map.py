from utils import randbool
from utils import random_point
from utils import random_cell

TREE_BONUS = 100
TREE_LOST = 50
UPGRADE_COST = 500
LIFE_COST = 10_000
CELL_TYPES = {
    'border': '⬛',
    'field': '🟩',
    'forest': '🌲',
    'river': '🌊',
    'repear': '🏥',
    'upgrade': '🔧',
    'fire': '🔥',
    'helicopter': '🚁',
    'tank': '🧺',
    'score': '🏆',
    'lives': '💗',
    'hospital': '🏥',
    'clouds': '⬜',
    'lightning': '🟥'    
}

class Map:

    def __init__(self, weidth, higth):
        self.weidth = weidth
        self.higth = higth
        self.cells = [[CELL_TYPES.get('field') for i in range(weidth)] for j in range(higth)]
        self.generate_forest(3, 10)
        self.generate_river(20)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()

    def print_map(self, helicopter, clouds):
        print(CELL_TYPES.get('border') * (self.weidth + 2))
        for ri in range(self.higth):
            print(CELL_TYPES.get('border'), end="")
            for ci in range(self.weidth):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == CELL_TYPES.get('clouds')):
                    print(CELL_TYPES.get('clouds'), end="")
                elif (clouds.cells[ri][ci] == CELL_TYPES.get('lightning')):
                    print(CELL_TYPES.get('lightning'), end="")
                elif (helicopter.x == ri and helicopter.y == ci):
                    print(CELL_TYPES.get('helicopter'), end="")
                else:
                    print(cell, end="")                
            print(CELL_TYPES.get('border'))
        print(CELL_TYPES.get('border') * (self.weidth + 2))
    
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.higth or y >= self.weidth):
            return False
        else: return True

    def generate_river(self, long_river):
        rc = random_point(self.weidth, self.higth)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = CELL_TYPES.get('river')
        while long_river > 0:
            rc2 = random_cell(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = CELL_TYPES.get('river')
                rx, ry = rx2, ry2
                long_river -= 1

    def generate_forest(self, r, mxr):
        for row in range(self.higth):
            for cell in range(self.weidth):
                if randbool(r, mxr):
                    self.cells[row][cell] = CELL_TYPES.get('forest')

    def gererate_tree(self):
        tree_update = 0
        cell = random_point(self.weidth, self.higth)
        cell_x, cell_y = cell[0], cell[1]
        while tree_update < 5:
            if (self.check_bounds(cell_x, cell_y) 
                and (self.cells[cell_x][cell_y] == CELL_TYPES.get('field')
                and self.cells[cell_x][cell_y] != CELL_TYPES.get('forest'))
                ):
                self.cells[cell_x][cell_y] = CELL_TYPES.get('forest')
                break
            tree_update += 1

    def generate_upgrade_shop(self):
        cell = random_point(self.weidth, self.higth)
        cell_x, cell_y = cell[0], cell[1]
        self.cells[cell_x][cell_y] = CELL_TYPES.get('upgrade')

    def generate_hospital(self):
        cell = random_point(self.weidth, self.higth)
        cell_x, cell_y = cell[0], cell[1]
        if self.cells[cell_x][cell_y] != CELL_TYPES.get('upgrade'):
            self.cells[cell_x][cell_y] = CELL_TYPES.get('hospital')
        else:
            self.generate_hospital()

    def add_fire(self):
        cell = random_point(self.weidth, self.higth)
        cell_x, cell_y = cell[0], cell[1]
        if self.cells[cell_x][cell_y] == CELL_TYPES.get('forest'):
            self.cells[cell_x][cell_y] = CELL_TYPES.get('fire')

    def update_fire(self, helicopter):
        for row in range(self.higth):
            for cell in range(self.weidth):
                value = self.cells[row][cell]
                if value == CELL_TYPES.get('fire'):
                    helicopter.score -= TREE_LOST
                    self.cells[row][cell] = CELL_TYPES.get('field')
        for i in range(10):
            self.add_fire()

    def process_helicopter(self, helicopter, clouds):
        helicopter_cell = self.cells[helicopter.get_x()][helicopter.get_y()]
        cloud_cell = clouds.cells[helicopter.get_x()][helicopter.get_y()]
        if (helicopter_cell == CELL_TYPES.get('river')):
            helicopter.tank = helicopter.maxtank
        elif (helicopter_cell == CELL_TYPES.get('fire') and helicopter.tank > 0):
             helicopter.tank -= 1
             helicopter.score += TREE_BONUS
             self.cells[helicopter.get_x()][helicopter.get_y()] = CELL_TYPES.get('forest')
        if (helicopter_cell == CELL_TYPES.get('upgrade') and helicopter.score >= UPGRADE_COST * helicopter.maxtank):
            helicopter.score -= UPGRADE_COST * helicopter.maxtank
            helicopter.maxtank += 1
        if (helicopter_cell == CELL_TYPES.get('hospital') and helicopter.score >= LIFE_COST):
            helicopter.score -= LIFE_COST
            helicopter.lives += 100
        if cloud_cell == CELL_TYPES.get('lightning'):
            helicopter.lives -= 1
            if (helicopter.lives == 0):
                helicopter.game_over()

    def export_data(self):
        return {
            'cells': self.cells
        }
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.weidth)] for j in range(self.higth)]                