from utils import randbool

CELL_TYPES = {
    'clouds': '⬜',
    'lightning': '🟥',
}

class Clouds:
    def __init__(self, weidth, higth):
        self.higth = higth
        self.weidth = weidth
        self.cells = [[0 for i in range(weidth)] for j in range(higth)]

    def update_clouds(self, r = 1, mxr = 30, g = 1, mxg = 10):
        for i in range(self.higth):
            for j in range(self.weidth):
                if randbool(r, mxr):
                    self.cells[i][j] = CELL_TYPES.get('clouds')
                    if randbool(g, mxg):
                        self.cells[i][j] = CELL_TYPES.get('lightning')
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {
            'cells': self.cells
        }
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.weidth)] for j in range(self.higth)]                