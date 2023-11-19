from random import randint as rand

def randbool(r, mxr):
    temp = rand(0, mxr)
    return (temp <= r)

def random_point(weidth, higth):
    t_weidth = rand(0, weidth - 1)
    t_higth = rand(0, higth - 1)
    return (t_higth, t_weidth)

def random_cell(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)