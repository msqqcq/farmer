

l = 3
substance = l* 2**(num_unlocked(Unlocks.Mazes) - 1)

def init():
	global substance
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)


def re_d(d):
	if d == East:
		return West
	if d == West:
		return East
	if d == North:
		return South
	if d == South:
		return North


def gk(ls=[]):
	if not ls or len(ls) != 2:
		if len(ls) == 1:
			loc = ls[0]
			return loc[0]*100000 + loc[1]+10000000
		return
	return ls[0][0]*35937 + ls[0][1]*1089 + ls[1][0]*33 + ls[1][1]


locs = []
locs_near = {}
mlen = l*l

last_loc = [0,0]

rs = {}
xr_locs = [] # 岔路口


def print_rs():
	return
	global rs
	r = ''
	for i in rs:
		r += str(i) + '->' + str(rs[i]) + '| '
	quick_print('len(rs): ', len(rs))
	quick_print('locs: ', locs)
	quick_print(r)
	quick_print('==============')
	quick_print('==============')
	quick_print('==============')

def get_near_locs(loc):
	s = []
	if loc[0] > 0:
		if can_move(West):
			s.append([loc[0]-1, loc[1]])
	if loc[0] < l-1:
		if can_move(East):
			s.append([loc[0]+1, loc[1]])
	if loc[1] > 0:
		if can_move(South):
			s.append([loc[0], loc[1]-1])
	if loc[1] < l-1:
		if can_move(North):
			s.append([loc[0], loc[1]+1])
	return s

def pick_near(loc):
	global locs
	global locs_near
	nears = locs_near[gk([loc])]
	for i in range(1, len(locs)+1):
		if locs[-i] in nears:
			return locs[-i]
	quick_print('pick_near: ', loc, 'nears: ', nears)
	return None

def is_near(l1, l2, direction):
	if direction == East:
		return l1[1] == l2[1] and l1[0] == l2[0] - 1
	if direction == West:
		return l1[1] == l2[1] and l1[0] == l2[0] + 1
	if direction == North:
		return l1[0] == l2[0] and l1[1] == l2[1] - 1
	if direction == South:
		return l1[0] == l2[0] and l1[1] == l2[1] + 1
	return False
		

def record(d):
	global last_loc
	global rs
	global locs
	if d not in [East, West, North, South]:
		last_loc = d
		locs.append(d)
		locs_near[gk([d])] = get_near_locs(d)
		return
	current_loc = [get_pos_x(), get_pos_y()]
	locs.append(current_loc)
	if current_loc not in locs_near:
		locs_near[gk([current_loc])] = get_near_locs(current_loc)
	if not last_loc:
		last_loc = locs[-1]
		

	if len(locs) == 2:
		rs[gk([last_loc, current_loc])] = d
		rs[gk([current_loc, last_loc])] = re_d(d)


		
	if len(locs) > 2:		
		for i in range(len(locs)-2):
			rs[gk([locs[i], current_loc])] = last_loc
			# if i == len(locs)-3:
			# 	rs[gk([current_loc, locs[i]])] = last_loc
			# else:
			# 	rs[gk([current_loc, locs[i]])] = pick_near(locs[i])
			
		rs[gk([last_loc, current_loc])] = d
		rs[gk([current_loc, last_loc])] = re_d(d)

		fix_loc = locs[-2]
		if not is_near(fix_loc, current_loc, d):
			rs[gk([fix_loc, current_loc])] = last_loc
			# rs[gk([current_loc, fix_loc])] = locs[-3]
			
	# print_rs()
	last_loc = current_loc


def get_routes(cur, destination):
	global rs
	k = gk([cur, destination])
	d = rs[k]

	routes = []
	while d not in [East, West, North, South]:
		r = rs[gk([d, destination])]
		routes.append(r)
		d = rs[gk([cur, d])]
	routes.append(d)
	return routes	


def move_to(cur, destination):
	if cur == destination:
		return

	reverse = True
	k = gk([cur, destination])
	if k not in rs:
		k = gk([destination, cur])
		if k not in rs:
			quick_print("No path found")
			return
		reverse = False
		t = cur
		cur = destination
		destination = t


	routes = get_routes(cur, destination)
	if reverse:
		for i in range(1,len(routes)+1):
			move(routes[-i])
		return
	for i in range(len(routes)):
		move(routes[i])
		
			

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

time = 0
def re_treasure():
	global time
	global substance
	if time == 300:
		return False
	use_item(Items.Weird_Substance, substance)
	time += 1
	return True
			
def go():
	global xr_locs
	global locs
	global mlen
	global last_loc
	global rs
	cur = [0,0]
	record(cur)
	ds = is_xr()

	d = ds.pop()
	if len(ds)>0:
		xr_locs.append([cur, ds])
	
	finish = False
	while True:
		last_loc = cur
		if get_entity_type() == Entities.Treasure:	
			re = re_treasure()
			if not re:
				harvest()
				finish = True
				break
			
		move(d)
		cur = [get_pos_x(), get_pos_y()]
		record(d)

		if mlen == len(locs):
			quick_print("跑图完成>>>>>>>>>>>>>>>")
			print_rs()
			break

		ds = is_xr()
		if len(ds) == 1:
			# 说明走到了尽头
			last_xr = xr_locs.pop()
			if not last_xr:
				quick_print("岔路完成>>>>>>>>>>>>>>>")
				continue
			last_xrloc = last_xr[0]
			last_ds = last_xr[1]
			d = last_ds.pop()
			if len(last_ds) > 0:
				xr_locs.append([last_xrloc, last_ds])
			move_to(cur, last_xrloc)
			cur = last_xrloc
			continue
		
		ds.remove(re_d(d))
		d = ds.pop()
		if len(ds) > 0:
			xr_locs.append([cur, ds])
		

	if not finish:
		while True:
			treasure_loc = measure()
			if treasure_loc:
				move_to(cur, treasure_loc)
				if get_entity_type() == Entities.Treasure:
					re = re_treasure()
					if not re:
						harvest()
						break
					cur = treasure_loc
				else:
					print_rs()
					quick_print("No treasure found, cur: ", cur, "treasure_loc: ", treasure_loc)
					k = gk([cur, treasure_loc])
					quick_print(k,':', rs[k])
					k = gk([cur, rs[k]])
					quick_print(k,':', rs[k])
					k = gk([cur, rs[k]])
					quick_print(k,':', rs[k])
					k = gk([cur, rs[k]])
					quick_print(k,':', rs[k])
					break
			else:
				quick_print("No treasure found")
				break

	
clear()
init()
go()
		
		