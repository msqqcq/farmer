from common import Entities, Items, Grounds, North, East, South, West, get_ground_type
from common import can_harvest, harvest, num_items, get_entity_type, move, use_item, till, plant, get_water, get_companion
from common import get_pos_x, get_pos_y


from run_ground import go_once, go, mv_loc, get_loc_str
from utils import run_with_count


# 4000/s

p_dict = {}

def init():
	mv_loc([5,5])
	harvest()
	if get_ground_type() != Grounds.Grassland:
		till()

def plant_and_log(p):
	if p:
		if p == Entities.Carrot and get_ground_type() != Grounds.Soil:
			till()
		elif p == Entities.Grass and get_ground_type() != Grounds.Grassland:
			till()
		plant(p)
	p_dict[get_loc_str()] = p

def cut():
	t, (x, y) = get_companion()
	if get_loc_str(x, y) not in p_dict:
		current_loc = [get_pos_x(), get_pos_y()]
		mv_loc([x, y])
		harvest()
		plant_and_log(t)
		mv_loc(current_loc)
		harvest()
	elif t != Entities.Tree and p_dict[get_loc_str(x, y)] != t:
		current_loc = [get_pos_x(), get_pos_y()]
		mv_loc([x, y])
		harvest()
		plant_and_log(t)
		mv_loc(current_loc)
		harvest()
	else:
		harvest()

def exec(time=None):
	init()
	if time:
		for _ in range(time):
			if get_water() < 0.75:
				use_item(Items.Water)
			if can_harvest():
				cut()
		return
	while True:
		if get_water() < 0.75:
			use_item(Items.Water)
		if can_harvest():
			cut()
			
run_with_count(exec)