map = {
	Entities.Grass:Items.Hay,
	Entities.Carrot:Items.Carrot,
	Entities.Pumpkin:Items.Pumpkin,
	Entities.Tree:Items.Wood,
	Entities.Bush:Items.Wood
}

def harvest_with_num():
	global map
	if not can_harvest():
		return None, None
	
	item = map[get_entity_type()]
	count = num_items(item)
	harvest()
	return item, num_items(item) - count
		
	
def run_with_count(run):
	items = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin]
	count = {}
	
	
	for i in items:
		count[i] = num_items(i)
		
	s = get_time()
	run()
	
	pass_time = get_time() - s
	if pass_time<1:
		pass_time =1
	
	for i in items:
		c = num_items(i) - count[i]
		
		quick_print(i, c, str(c//pass_time)+'/s')
	
	
	
	