from common import Entities, Items, North, East, South, West
from common import can_harvest, harvest, num_items, get_entity_type, get_pos_x, get_pos_y, get_world_size

d = North
routes = []
world_size = get_world_size()

def reverse_d():
	global d
	if d == North:
		d = South
	else:
		d = North
		
def mv(dir):
	global routes
	move(dir)
	routes.append(dir)
	
def get_shortest_direction(curr, target, world_size, is_x_axis):
	max_steps = (world_size + 1) // 2
	steps = target - curr
	if steps > 0:
		if steps > max_steps:
			steps = world_size - steps
			if is_x_axis:
				direction = West 
			else:
				direction = South
		else:
			if is_x_axis:
				direction = East 
			else:
				direction = North
	else:
		steps = abs(steps)
		if steps > max_steps:
			steps = world_size - steps
			if is_x_axis:
				direction = East 
			else:
				direction = North
		else:
			if is_x_axis:
				direction = West 
			else:
				direction = South
	if steps == 0:
		return None, 0
	return direction, steps
	
def do_nothing():
	pass

def mv_loc(loc, do_something=do_nothing):
	if loc in [East, West, North, South]:
		move(loc)
		return
	global world_size
	routes = []
	
	# Handle X movement
	dir_x, steps_x = get_shortest_direction(get_pos_x(), loc[0], world_size, True)
	if dir_x:
		for _ in range(steps_x):
			routes.append(dir_x)
	
	# Handle Y movement
	dir_y, steps_y = get_shortest_direction(get_pos_y(), loc[1], world_size, False)
	if dir_y:
		for _ in range(steps_y):
			routes.append(dir_y)
	
	for direction in routes:
		do_something()
		move(direction)

def get_loc_str(x=get_pos_x(), y=get_pos_y()):
	return str(x) + str(y)

def go_once(do_something, size=get_world_size()):
	global d
	global routes
	routes = []
	for _ in range(size):
		for _ in range(size - 1):
			do_something()
			mv(d)
		do_something()
		reverse_d()
		mv(East)
	mv_loc([0,0])
	routes[-1] = [0,0]
	return routes
		
def go(do_something):
	global routes
	while True:
		for i in range(len(routes)):
			do_something()
			move(routes[i])

def snake_routes(l = get_world_size()):
	routes = []
	
	f = True
	for x in range(1, l):
		if f:
			routes.append(East)
			for _ in range(x):
				routes.append(North)
			
			for _ in range(x):
				routes.append(West)
			routes.append(North)
			for _ in range(x+1):
				routes.append(East)
			f = False
		else:
			for _ in range(x):
				routes.append(South)
			f = True
	if l%2==0:
		routes = routes[:-1-l]
	return routes