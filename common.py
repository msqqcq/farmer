from enum import Enum, auto

# 方向枚举
class Direction(Enum):
	North = auto()
	East = auto()
	South = auto()
	West = auto()

# 便于直接导入使用
North = Direction.North
East = Direction.East
South = Direction.South
West = Direction.West

# 实体枚举
class Entities(Enum):
	Grass = auto()
	Carrot = auto()
	Tree = auto()
	Bush = auto()
	Pumpkin = auto()
	Dead_Pumpkin = auto()
	Cactus = auto()

# 物品枚举
class Items(Enum):
	Hay = auto()
	Carrot = auto()
	Wood = auto()
	Water = auto()
	Pumpkin = auto()
	Weird_Substance = auto()
	Fertilizer = auto()
	Power = auto()

class Grounds(Enum):
	Grassland = auto()
	Soil = auto()
	
# 以下为函数空实现（pass），避免覆盖内置函数/类型

def can_harvest():
	pass

def change_hat(*args, **kwargs):
	pass

def clear():
	pass

def do_a_flip():
	pass

def get_companion():
	pass

def get_cost(*args, **kwargs):
	pass

def get_entity_type():
	pass

def get_ground_type():
	pass

def get_pos_x():
	pass

def get_pos_y():
	pass

def get_tick_count():
	pass

def get_time():
	pass

def get_water():
	pass

def get_world_size():
	pass

def harvest():
	pass

def move(direction):
	pass

def num_items(item):
	pass

def num_unlocked():
	pass

def pet_the_piggy():
	pass

def plant(entity):
	pass

def quick_print(*args, **kwargs):
	print(*args, **kwargs)

def till():
	pass

def unlock(*args, **kwargs):
	pass

def use_item(item):
	pass

def measure(loc):
	pass


def gr():
	d = {}
	for i in range(32):
		for j in range(32):
			for m in range(32):
				for n in range(32):
					d[i*35937 + j*1089 + m*33 + n] = 0
					
	for i in range(32):
		for j in range(32):
			k = i*100000 + j + 10000000
			if k in d.keys():
				print("!!!!!!!!")
				return

if __name__ == "__main__":
	gr()

