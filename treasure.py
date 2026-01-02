def drone_function():
	while True:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, get_world_size())
		direction = 0
		corect = 0
		while corect == 0:
			if direction == 0:
				if move(North):
					direction = 3
				else:
					direction = 1
			elif direction == 3:
				if move(West):
					direction = 2
				else:
					direction = 0
			elif direction == 2:
				if move(South):
					direction = 1
				else:
					direction = 3
			elif direction == 1:
				if move(East):
					direction = 0
				else:
					direction = 2
			if get_entity_type() == Entities.Treasure:
				corect = 1
				harvest()
while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size())
	corect = 0
	direction = 0
	while corect == 0:
		if direction == 0:
			if move(North):
				direction = 1
			else:
				direction = 3
		elif direction == 1:
			if move(East):
				direction = 2
			else:
				direction = 0
		elif direction == 2:
			if move(South):
				direction = 3
			else:
				direction = 1
		elif direction == 3:
			if move(West):
				direction = 0
			else:
				direction = 2
		if get_entity_type() == Entities.Treasure:
			corect = 1
			harvest()
		spawn_drone(drone_function)
