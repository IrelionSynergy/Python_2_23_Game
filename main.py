from map import Map
from helicopter import Helicopter as helicopter
import time
import os
from pynput import keyboard

# 🌲⬛🟩🌊🚁🔥🏥♥🚰🔧☁️⚡🏆

__TICK_SLEEP = 0.05
__TREE_UPDATE = 50
__FIRE_UPDATE = 100
__MAP_WIDTH, __MAP_HEIGTH = 20, 20
TICK = 1
MOVES = {
    'w': (-1, 0),
    'd': (0, 1),
    's': (1, 0),
    'a': (0, -1)
}

map = Map(__MAP_WIDTH, __MAP_HEIGTH)


helicopter = helicopter(__MAP_WIDTH, __MAP_HEIGTH)



def process_key(key):
    global helicopter
    c = key.char    
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicopter.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


while True:
    os.system('cls')
    print(TICK)
    map.process_helicopter(helicopter)
    helicopter.print_stats()
    map.print_map(helicopter)
    TICK += 1
    time.sleep(__TICK_SLEEP)
    if(TICK % __TREE_UPDATE == 0):
        map.gererate_tree()
    if(TICK % __FIRE_UPDATE == 0):
        map.update_fire()