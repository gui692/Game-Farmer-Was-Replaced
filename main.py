def drown_harvest():
	while True:
			for i in range(2):
				for n in range(get_world_size()):
					harvest()
					if i == 1 and n % 3 == 1:
						use_item(Items.Weird_Substance)
					move(North)
				move(East)
			for i in range(2):
				move(West)

def drown_harvest_tree():
	while True:
			for i in range(2):
				for n in range(get_world_size()):
					harvest()
					if (i + n) % 2 == 0:
						plant(Entities.Tree)
						if get_water() < 0.1:
							use_item(Items.Water)
						if i == 1 and n % 3 == 1:
							use_item(Items.Weird_Substance)
					move(North)
				move(East)
			for i in range(2):
				move(West)



#for i in range(7):
#	spawn_drone(drown_harvest)
#	for n in range(2):
#		move(East)
def sunflower_farm():
	position = 0
	petal = []
	if get_ground_type() == Grounds.Grassland:
			for num in range(get_world_size()):
				till()
				move(North)
	for n in range(get_world_size()):
		if get_ground_type() == Grounds.Soil and measure() == None:
			plant(Entities.Sunflower)
			if get_water() < 0.1:
				use_item(Items.Water)
			petal.append(measure())
		move(North)
		while position == 0 and len(petal) == get_world_size():
			for counter in range(15, 9, -1):
				for loop in range(get_world_size()):
					if petal[loop] == counter:
						for moving in range(loop - get_pos_y()):
							move(North)
						while not can_harvest():
							print("waiting now ...")
						harvest()
				for moving in range(get_pos_y()):
					move(South)
			position = 1
	for i in range(get_world_size()):
		harvest()
		move(North)

for i in range(15):
	spawn_drone(drown_harvest_tree)
	for n in range(2):
		move(East)
move(East)
while True:
	sunflower_farm()