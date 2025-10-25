from common import Entities, Items, Grounds, North, East, South, West, get_ground_type, get_world_size
from common import can_harvest, harvest, num_items, get_entity_type, move, use_item, till, plant, get_water, get_companion
from common import get_pos_x, get_pos_y, measure, clear


from run_ground import go_once, go, mv_loc, get_loc_str
from utils import run_with_count


l = get_world_size()


def plant_cactus():
	if get_ground_type() == Grounds.Soil:
		plant(Entities.Cactus)
	else:
		till()
		plant(Entities.Cactus)


def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0][0]
	left = []
	right = []
	for i in range(1, len(arr)):
		if arr[i][0] <= pivot:
			left.append(arr[i])
		else:
			right.append(arr[i])
	return quicksort(left) + [arr[0]] + quicksort(right)

def get_routes(arr, direction):
	global l
	t = None
	routes = []
	for i in range(l-1):
		if arr[i][0] > arr[i+1][0]:
			t = arr[i][0]
			arr[i][0] = arr[i+1][0]
			arr[i+1][0] = t
			routes.append([arr[i][1], direction])
	return routes
			

def sort_x(l):
	y = get_pos_y()
	arr = []
	for i in range(l):
		plant_cactus()
		arr.append([measure(), [i,y]])
		move(East)

	routes = get_routes(arr, East)
	while routes:
		for route in routes:
			mv_loc(route[0])
			swap(route[1])
		routes = get_routes(arr, East)
	
def sort_y(l):
	x = get_pos_x()
	arr = []
	for i in range(l):
		arr.append([measure(), [x,i]])
		move(North)

	routes = get_routes(arr, North)
	while routes:
		for route in routes:
			mv_loc(route[0])
			swap(route[1])
		routes = get_routes(arr, North)


def exec():
	for i in range(l):
		mv_loc([0,i])
		sort_x(l)
	
	for i in range(l):
		mv_loc([i,0])
		sort_y(l)
	
	harvest()
	
	
run_with_count(exec)
			
