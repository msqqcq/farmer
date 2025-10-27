from run_ground import go_once, go, mv_loc, get_loc_str
from utils import run_with_count

def plant_sunflower():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Sunflower)
    while get_water() < 0.75:
        use_item(Items.Water)
    # while measure() < 15:
    #     harvest()
    #     plant(Entities.Sunflower)

l = get_world_size()

def y_plant():
    global l
    for _ in range(l-1):
        move(North)
        plant_sunflower()
        

def plantx():
    global l
    for _ in range(l-1):
        spawn_drone(y_plant)
        plant_sunflower()
        move(East)
    plant_sunflower()
    y_plant()
    move(North)
    move(East)
    
def y_cut(p=True):
    global l
    for _ in range(l-1):
        move(North)
        while not can_harvest():
            pass
        harvest()
        if p:
            plant_sunflower()
        
def y_cut_f():
    y_cut(False)

def cut(p=True):
    global l
    for _ in range(l-1):
        if p:
            spawn_drone(y_cut)
        else:
            spawn_drone(y_cut_f)
        while not can_harvest():
            pass
        harvest()
        if p:
            plant_sunflower()
        move(East)
    while not can_harvest():
        pass
    harvest()
    if p:
        plant_sunflower()
    y_cut(p)
    move(North)
    move(East)

def go():
    plantx()
    for _ in range(2):
        while num_drones() != 1:
            pass
        cut()
    cut(False)



clear()
run_with_count(go)