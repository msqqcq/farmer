from run_ground import go_once, go, mv_loc, get_loc_str
from utils import run_with_count


deads = {}

def plant_pumpkin():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Pumpkin)
    while get_water() < 0.5:
        use_item(Items.Water)

def gk(x,y):
	return x*33 + y

def log_dead():
    global deads
    x, y = get_pos_x(), get_pos_y()
    k = gk(x,y)
    if not can_harvest():
        deads[k] = (x, y)
        plant(Entities.Pumpkin)
    else:
        if k in deads:
            deads.pop(k)

def mv_to(x, y):
    cy = get_pos_y()
    if y == cy:
        return
    if y > cy:
        move(North)
    elif y < cy:
        move(South)
    mv_to(x,y)

def mvn():
    global deads
    l = get_world_size()/2
    for i in range(l):
        plant_pumpkin()
        move(North)

    for i in range(l):
        move(South)
        log_dead()

    while deads:
        copy = []
        for key in deads:
            copy.append(key)
        for k in copy:
            mv_to(deads[k][0], deads[k][1])
            log_dead()

def mvs():
    global deads
    l = get_world_size()/2
    for i in range(l):
        plant_pumpkin()
        move(South)

    for i in range(l):
        move(North)
        log_dead()

    while deads:
        copy = []
        for key in deads:
            copy.append(key)
        for k in copy:
            mv_to(deads[k][0], deads[k][1])
            log_dead()

def go():
    for _ in range(get_world_size()-1):
        spawn_drone(mvn)
        move(South)
        spawn_drone(mvs)
        move(North)
        move(East)

    spawn_drone(mvn)
    move(South)
    mvs()

    mv_loc([0,0])
    while num_drones() != 1:
        pass
    if can_harvest():
        harvest()


def run():
    for _ in range(2):
        go()
run_with_count(run)