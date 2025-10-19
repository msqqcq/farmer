from run_ground import go_once, go, mv_loc
from utils import harvest_with_num, run_with_count


p_loc = []
p = False
routes = []
def get_plant():
	global p
	p = not p
	if p:
		return Entities.Tree
	else:
		return Entities.Carrot
	

def init():
	till()
	p = get_plant()
	plant(p)
	p_loc.append(p)



def watering():
	if get_water()<=0.75:
		use_item(Items.Water)

def run(d, p):
	if can_harvest():
		harvest()
		plant(p)
	else:
		#watering()
		pass
		
	move(d)
	
def exec_once():
	global routes
	for i in range(len(routes)):
		run(routes[i], p_loc[i])
	if can_harvest():
		harvest()
		plant(p_loc[i+1])
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
routes = go_once(init, 10)
run_with_count(exec_test)