
def init():
	clear()
	set_world_size(5)
	change_hat(Hats.Dinosaur_Hat)

def re_d(d):
	if d == East:
		return West
	if d == West:
		return East
	if d == North:
		return South
	if d == South:
		return North
	return d

def gk(ls=[]):
	return ls[0]*100000 + ls[1]+10000000

def get_routes():
	routes = [North]
	d = North
	size=get_world_size()
	for _ in range(size):
		for _ in range(size - 2):
			routes.append(d)
		routes.append(East)
		d = re_d(d)
	routes[-1] = South
	for _ in range(size - 1):
		routes.append(West)
	return routes

locs = []

def mv(d):
	global locs
	f = move(d)
	if f:
		locs.pop(0)
	return f

def move_to(x,y):
	global locs
	cur_x = get_pos_x()
	cur_y = get_pos_y()

	if x == cur_x and y == cur_y:
		return
	locs.append([cur_x, cur_y])
	if x > cur_x:
		if not mv(East):
			for d in [North, South]:
				if mv(d):
					break
		move_to(x,y)
		return
	if x < cur_x:
		if not mv(West):
			for d in [North, South]:
				if mv(d):
					break
		move_to(x,y)
		return
	if y > cur_y:
		if not mv(North):
			for d in [East, West]:
				if momvve(d):
					break
		move_to(x,y)
		return
	if y < cur_y:
		if not mv(South):
			for d in [East, West]:
				if mv(d):
					break
		move_to(x,y)
		return

	


def phase1():
	x,y = measure()
	move_to(x,y)
	if len(locs) == get_world_size()*3:
		return

	


def go():
	init()
	phase1()
	move_to(0,0)
	routes = get_routes()
	while True:
		for i in routes:
			if not move(i):
				quick_print("move failed")
				change_hat(Hats.Purple_Hat)
				return
	
go()