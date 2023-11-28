from map import Map
from clouds import Clouds
from pynput import keyboard
from helicopter import Helicopter as helicopter
import time
import os
import json

__TICK_SLEEP = 0.1
__TREE_UPDATE = 50
__FIRE_UPDATE = 150
__CLOUD_UPDATE = 100
__MAP_WIDTH, __MAP_HEIGTH = 20, 20
TICK = 1
MOVES = {
    'w': (-1, 0),
    'd': (0, 1),
    's': (1, 0),
    'a': (0, -1)
}

map = Map(__MAP_WIDTH, __MAP_HEIGTH)
clouds = Clouds(__MAP_WIDTH, __MAP_HEIGTH)
helicopter = helicopter(__MAP_WIDTH, __MAP_HEIGTH)

def process_key(key):
    global helicopter, TICK, clouds, map
    c = key.char    
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicopter.move(dx, dy)
    if c == 'f':
        data = {
            'helicopter': helicopter.export_data(),
            'clouds': clouds.export_data(),
            'map': map.export_data(),
            'tick': TICK
        }
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    if c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            TICK = data['tick'] or 1
            helicopter.import_data(data['helicopter'])
            map.import_data(data['map'])
            clouds.import_data(data['clouds'])    

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

while True:
    os.system('cls')
    map.process_helicopter(helicopter, clouds)
    helicopter.print_stats()
    map.print_map(helicopter, clouds)
    print(TICK)
    TICK += 1
    time.sleep(__TICK_SLEEP)
    if(TICK % __TREE_UPDATE == 0):
        map.gererate_tree()
    if(TICK % __FIRE_UPDATE == 0):
        map.update_fire(helicopter)
    if(TICK % __CLOUD_UPDATE == 0):
        clouds.update_clouds()