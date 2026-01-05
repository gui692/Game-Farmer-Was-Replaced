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

def swap_inventory(cactus_inventory, index_a, index_b):
	temp = cactus_inventory[index_a]
	cactus_inventory[index_a] = cactus_inventory[index_b]
	cactus_inventory[index_b] = temp

def cactus_farm(count):
	cactus_inventory = []
	cactus_array = [0,0,0,0,0,0,0,0,0]
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
	#    for i in range(len(cactus_inventory)):
	#        if n + 1 == cactus_inventory[i]:
	#            cactus_array[n] += 1
	total = len(cactus_inventory)
	target_index = 0
	for n in range(10):
		while target_index < total:
			found_index = -1
			for i in range(target_index, total):
				if cactus_inventory[i] == n:
					found_index = i
					break
			if found_index == -1:
				break
			target_x = target_index // count
			target_y = target_index % count
			x = found_index // count
			y = found_index % count
			moving_x(x, get_pos_x())
			moving_y(y, get_pos_y())
			while y < target_y:
				swap(North)
				move(North)
				y += 1
				swap_inventory(cactus_inventory, x * count + y, x * count + (y - 1))
			while y > target_y:
				swap(South)
				move(South)
				y -= 1
				swap_inventory(cactus_inventory, x * count + y, x * count + (y + 1))
			while x > target_x:
				swap(West)
				move(West)
				x -= 1
				swap_inventory(cactus_inventory, x * count + y, (x + 1) * count + y)
			while x < target_x:
				swap(East)
				move(East)
				x += 1
				swap_inventory(cactus_inventory, x * count + y, (x - 1) * count + y)
			target_index += 1
			moving_x(0, get_pos_x())
			moving_y(0, get_pos_y())
		if target_index >= total:
			break
			

while True:
    cactus_farm(32)
    harvest()
