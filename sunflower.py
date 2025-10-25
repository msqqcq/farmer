from common import Entities, Items, Grounds, North, East, South, West, get_ground_type
from common import can_harvest, harvest, num_items, get_entity_type, move, use_item, till, plant, get_water, get_companion
from common import get_pos_x, get_pos_y, measure


from run_ground import go_once, go, mv_loc, get_loc_str
from utils import run_with_count

def plant_sunflower():
	plant(Entities.Sunflower)
	while measure() < 15:
		harvest()
		plant(Entities.Sunflower)

def init():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant_sunflower()
	

def exec(time=2):
	mv_loc([0,0])
	routes = go_once(init, 4)
	if time:
		for _ in range(time):
			for i in range(len(routes)):
				#if get_water() < 0.75:
					#use_item(Items.Water)
				if can_harvest():
					harvest()
					plant_sunflower()
				mv_loc(routes[i])
	else:
		while True:
			for i in range(len(routes)):
				#if get_water() < 0.75:
					#use_item(Items.Water)
				if can_harvest():
					harvest()
					plant_sunflower()
				mv_loc(routes[i])
			
def init2():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)

def exec2(time=2):
	mv_loc([0,0])
	routes = go_once(init2, 6)
	if time:
		for _ in range(time):
			for i in range(len(routes)):
				if get_water() < 0.75:
					use_item(Items.Water)
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
				mv_loc(routes[i])
	else:
		while True:
			for i in range(len(routes)):
				if get_water() < 0.75:
					use_item(Items.Water)
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
				mv_loc(routes[i])

run_with_count(exec2)