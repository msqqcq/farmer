from run_ground import mv_loc
from utils import run_with_count

l = get_world_size()

exec_times = 100

def gk(x,y):
    return x*33 + y

p_dict_temp = {
    gk(l-1,l-1):None,
    gk(l-1,1):None,
    gk(1,l-1):None,
    gk(1,0):None,
    gk(1,1):None,
    gk(2,l-1):None,
    gk(2,0):None,
    gk(2,1):None,
    gk(3,l-1):None,
    gk(3,0):None,
    gk(3,1):None,
    gk(5,1):None,
    gk(5,l-1):None,
}
p_dict = {}



def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
    while get_water() < 0.75:
		use_item(Items.Water)
	plant(Entities.Carrot)

def plant_and_log(x,y,p):
    harvest()
    if p:
        if p == Entities.Carrot and get_ground_type() != Grounds.Soil:
            till()
        elif p == Entities.Grass and get_ground_type() != Grounds.Grassland:
            till()
        plant(p)
    k = gk(x, y)
    if k in p_dict:
        p_dict[k] = p


def cut():
    if can_harvest():
        current_loc = [get_pos_x(), get_pos_y()]
        t, (x, y) = get_companion()
        k = gk(x, y)
        if k in p_dict:
            if p_dict[k] != t:
                mv_loc([x, y])
                plant_and_log(x, y, t)
                mv_loc(current_loc)
        else:
            mv_loc([x, y])
            plant_and_log(x, y, t)
            mv_loc(current_loc)
        harvest()
        plant_carrot()

def go(time=exec_times):
    plant_carrot()
    t, (x, y) = get_companion()
    for k in p_dict_temp:
        p_dict[k+(x*33+y)] = Entities.Grass

    for _ in range(4):
        move(East)
    plant_carrot()
    for _ in range(4):
        move(West)


    for _ in range(time):
        cut()
        for _ in range(4):
            move(East)
        cut()
        for _ in range(4):
            move(West)


def run():
    ps = []
    i = l//8
    j = l//4
    x = 0
    y = 0
    for _ in range(j):
        for _ in range(i):
            ps.append([x, y])
            x += 8
        x = 0
        y += 4

    for j in range(len(ps)-1):
        mv_loc(ps[j])
        spawn_drone(go)
    mv_loc(ps[-1])
    go()

clear()
run_with_count(run)



