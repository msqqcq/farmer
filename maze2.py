l = 5
substance = l* 2**(num_unlocked(Unlocks.Mazes) - 1)

def init():
	clear()
	global substance
	#quick_print(substance)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)
	

def check_and_harvest():
	global substance
	init_num = num_items(Items.Weird_Substance)
	i = num_items(Items.Gold)
	cur = [get_pos_x(), get_pos_y()]
	quick_print("cur", cur)
	while True:
		if not measure():
			break
		if get_entity_type() == Entities.Treasure:
			if num_drones() != 25:
				# quick_print("num_drones()", num_drones())
				continue
			cur_num = num_items(Items.Weird_Substance)
			if  init_num - cur_num == 300*substance:
				harvest()
				quick_print(init_num - cur_num)
				quick_print(num_items(Items.Gold) - i)
				break
			else:
				if not use_item(Items.Weird_Substance, substance):
					if can_harvest():
						quick_print(max_drones())
						harvest()
						quick_print(init_num - cur_num)
						quick_print(num_items(Items.Gold) - i)
						break
			

def re_d(d):
	if d == East:
		return West
	if d == West:
		return East
	if d == North:
		return South
	if d == South:
		return North


def is_xr():
	n = []
	if can_move(East):
		n.append(East)
	if can_move(West):
		n.append(West)
	if can_move(North):
		n.append(North)
	if can_move(South):
		n.append(South)
	return n 


def gk(ls=[]):
	if not ls or len(ls) != 2:
		if len(ls) == 1:
			loc = ls[0]
			return loc[0]*100000 + loc[1]+10000000
		return
	return ls[0][0]*35937 + ls[0][1]*1089 + ls[1][0]*33 + ls[1][1]


def go_east():
	go_d(East)
def go_west():
	go_d(West)
def go_north():
	go_d(North)
def go_south():
	go_d(South)


last_d = None
def go_d(direction):
	global last_d
	move(direction)
	last_d = direction
	if num_drones() >= 25:
		quick_print("num_drones()", num_drones())
		quick_print("=======")
		quick_print("=======")
		quick_print("=======")
		quick_print("=======")
		check_and_harvest()
	else:
		go()
	

def go():
	global last_d
	if not measure():
			return
	# cur = [get_pos_x(), get_pos_y()]
	# k = gk([cur])
	# direction=None
	# if k in xr_ds:
	#	 if len(xr_ds[k])>0:
	#		 direction = xr_ds[k].pop()
	# if direction:
	#	 move(direction)
	# else:
	#	 spawn_drone(check_and_harvest)
	
	ds = is_xr()

	if len(ds) == 1:
		# spawn_drone(check_and_harvest)
		if last_d == re_d(ds[0]):
			check_and_harvest()
		else:
			# spawn_drone(check_and_harvest)
			# move(ds[0])
			# last_d = ds[0]
			# go()
			if ds[0] == East:
				spawn_drone(go_east)
			elif ds[0] == West:
				spawn_drone(go_west)
			elif ds[0] == North:
				spawn_drone(go_north)
			elif ds[0] == South:
				spawn_drone(go_south)
			check_and_harvest()

	else:
		if re_d(last_d) in ds:
			ds.remove(re_d(last_d))
		for d in ds:
			if d == East:
				spawn_drone(go_east)
			elif d == West:
				spawn_drone(go_west)
			elif d == North:
				spawn_drone(go_north)
			elif d == South:
				spawn_drone(go_south)
		check_and_harvest()

for i in range(100):
	while num_drones() != 1:
		pass
	init()
	go()