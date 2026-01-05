def moving(target_x, target_y):
	while get_pos_x() < target_x:
		move(East)
	while get_pos_x() > target_x:
		move(West)
	while get_pos_y() < target_y:
		move(North)
	while get_pos_y() > target_y:
		move(South)

def pampkin_farm(portrait, landscape):
	first_psition = [get_pos_x(), get_pos_y()]
	while True:
		possiblity = 0
		for n in range(portrait):
			for i in range(landscape):
				if get_ground_type() == Grounds.Grassland:
					till()
				elif not can_harvest():
					plant(Entities.Pumpkin)
				elif can_harvest():
					possiblity += 1
				move(North)
			moving(get_pos_x(), first_psition[1])
			move(East)
		if possiblity == portrait * landscape:
			break
		moving(first_psition[0], first_psition[1])

def pampkin_farm_runner():
    pampkin_farm(1, 32)

def carrot_farm_runner():
	carrot_farm(1, 32)

def carrot_farm(portrait, landscape):
	first_psition = [get_pos_x(), get_pos_y()]
	while True:
		for n in range(portrait):
			for i in range(landscape):
				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
				elif can_harvest():
					harvest()
					if get_water() < 0.1:
						use_item(Items.Water)
					plant(Entities.Carrot)
				move(North)
			moving(get_pos_x(), first_psition[1])
			if not portrait == 1:
				move(East)
		moving(first_psition[0], first_psition[1])


# while True:
# 	for i in range(31):
# 		spawn_drone(pampkin_farm_runner)
# 		for n in range(1):
# 			move(East)
# 	pampkin_farm_runner()
# 	moving(0, 0)
# 	while num_drones() != 1:
# 		pass
# 	harvest()


while True:
	for i in range(31):
		spawn_drone(carrot_farm_runner)
		for n in range(1):
			move(East)
	carrot_farm_runner()