from common import Entities, Items, Grounds, North, East, South, West, get_ground_type
from common import can_harvest, harvest, num_items, get_entity_type, move, use_item, till, plant, get_water, get_companion


from run_ground import go_once, go, mv_loc, get_loc_str
from utils import harvest_with_num, run_with_count


p_loc = []
p_dict = {}
pt = False
routes = []
def get_plant():
	global pt
	pt = not pt
	if pt:
		return Entities.Tree
	else:
		return None

def plant_and_log(p):
	if p:
		if p == Entities.Carrot and get_ground_type() != Grounds.Soil:
			till()
		elif get_ground_type() != Grounds.Grassland:
			till()
		plant(p)
	p_dict[get_loc_str()] = p

def init():
	p = get_plant()
	plant_and_log(p)
	p_loc.append(p)

def cut():
	t, (x, y) = get_companion()
	if t != Entities.Tree and get_loc_str(x, y) in p_dict and p_dict[get_loc_str(x, y)] != t and p_dict[get_loc_str(x, y)] != Entities.Tree:
		current_loc = [get_pos_x(), get_pos_y()]
		mv_loc([x, y])
		harvest()
		plant_and_log(t)
		mv_loc(current_loc)
		harvest()
	else:
		harvest()
		

def watering():
	if get_water()<=0.75:
		use_item(Items.Water)

def run(d, p):
	if p and can_harvest():
		cut()
		plant_and_log(p)
	else:
		#watering()
		pass
		
	move(d)
	
def exec_once():
	global routes
	for i in range(len(routes)):
		run(routes[i], p_loc[i])
	if p_loc[i+1] and can_harvest():
		harvest()
		plant_and_log(p_loc[i+1])
	else:
		#watering()
		pass
	mv_loc([0,0])
	
def exec_test(time=3):
	for i in range(time):
		exec_once()
	 
def exec():
	#print(len(routes),len(p_loc))
	
	while True:
		exec_once()
		
		

#go_once(harvest)
clear()
routes = go_once(init, 9)
run_with_count(exec_test)