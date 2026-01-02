def moving_x(target_x, current_x):
	if target_x > current_x:
		for i in range(target_x - current_x):
			move(East)
	elif target_x < current_x:
		for i in range(current_x - target_x):
			move(West)
def moving_y(target_y, current_y):
	if target_y > current_y:
		for i in range(target_y - current_y):
			move(North)
	elif target_y < current_y:
		for i in range(current_y - target_y):
			move(South)

def cactus_farm(count):
	cactus_inventory = []
	cactus_array = [0,0,0,0,0,0,0,0,0]
	next_target_x = 0
	next_target_y = 0
	if get_ground_type() == Grounds.Grassland:
		for n in range(count):
			for i in range(count):
				till()
				move(North)
			for i in range(count):
				move(South)
			move(East)
		for n in range(count):
			move(West)
	for n in range(count):
		for i in range(count):
			plant(Entities.Cactus)
			cactus_inventory.append(measure())
			move(North)
		for i in range(count):
			move(South)
		move(East)
	for n in range(count):
		move(West)
	#for n in range(9):
		#for i in range(len(cactus_inventory)):
			#if n + 1 == cactus_inventory[i]:
				#cactus_array[n] += 1
	for n in range(10):
		for i in range(len(cactus_inventory)):
			if cactus_inventory[i] == n:
				x = i // count
				y = i % count
				moving_x(x, get_pos_x())
				moving_y(y, get_pos_y())

				if y < next_target_y:
					for j in range(next_target_y - y):
						swap(North)
						move(North)
						y += 1
						temp = cactus_inventory[x * count + y]
						cactus_inventory[x * count + y] = cactus_inventory[x * count + (y - 1)]
						cactus_inventory[x * count + (y - 1)] = temp
				if x < next_target_x:
					for j in range(next_target_x - x):
						swap(East)
						move(East)
						x += 1
						temp = cactus_inventory[x * count + y]
						cactus_inventory[x * count + y] = cactus_inventory[(x - 1) * count + y]
						cactus_inventory[(x - 1) * count + y] = temp
				else:
					for j in range(x - next_target_x):
						swap(West)
						move(West)
						x -= 1
						temp = cactus_inventory[x * count + y]
						cactus_inventory[x * count + y] = cactus_inventory[(x + 1) * count + y]
						cactus_inventory[(x + 1) * count + y] = temp
				if not y < next_target_y:
					for j in range(y - next_target_y):
						swap(South)
						move(South)
						y -= 1
						temp = cactus_inventory[x * count + y]
						cactus_inventory[x * count + y] = cactus_inventory[x * count + (y + 1)]
						cactus_inventory[x * count + (y + 1)] = temp


				if next_target_y == 0:
					next_target_y = next_target_x + 1
					next_target_x = 0
				else:
					next_target_y -= 1
					next_target_x += 1
				while (next_target_y >= count or next_target_x >= count) and not (next_target_y * next_target_x > count * count):
					if next_target_y == 0:
						next_target_y = next_target_x + 1
						next_target_x = 0
					next_target_y -= 1
					next_target_x += 1
					
				moving_x(0, get_pos_x())
				moving_y(0, get_pos_y())
			


cactus_farm(5)
harvest()