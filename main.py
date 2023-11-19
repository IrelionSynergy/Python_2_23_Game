from map import Map
from helicopter import Helicopter
import time
import os

# 🌲⬛🟩🌊🚁🔥🏥♥🚰🔧☁️⚡🏆

__TICK_SLEEP = 0.05
__TREE_UPDATE = 50
__FIRE_UPDATE = 100
__MAP_WIDTH, __MAP_HEIGTH = 20, 20
TICK = 1

map = Map(__MAP_WIDTH, __MAP_HEIGTH)
map.generate_forest(3, 10)
map.generate_river(20)
map.generate_river(10)

helicopter = Helicopter(__MAP_WIDTH, __MAP_HEIGTH)

while True:
    os.system('cls')
    print(TICK)
    map.print_map(helicopter)
    TICK += 1
    time.sleep(__TICK_SLEEP)
    if(TICK % __TREE_UPDATE == 0):
        map.gererate_tree()
    if(TICK % __FIRE_UPDATE == 0):
        map.update_fire()