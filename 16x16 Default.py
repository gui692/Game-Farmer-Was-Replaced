while True:
	list = [0,0,0,0]
	for i in range(get_world_size()):
		for n in range(get_world_size()):
			if i < 6 or 9 < i:
				if n < 6 or 9 < n:
					if not can_harvest():
						plant(Entities.Pumpkin)
						if n < 6 and i < 6:
							list[0] += 1
						elif 9 < n and i < 6:
							list[1] += 1
						elif n < 6 and 9 < i:
							list[2] += 1
						elif 9 < n and 9 < i:
							list[3] += 1
					if (n == 5 or n == 15) and (i == 5 or i == 15):
						if (n == 5 and i == 5) and (list[0] == 0):
							harvest()
						elif (n == 15 and i == 5) and (list[1] == 0):
							harvest()
						elif (n == 5 and i == 15) and (list[2] == 0):
							harvest()
						elif (n == 15 and i == 15) and (list[3] == 0):
							harvest()
				else:
					if can_harvest():
						harvest()
						if (n + i) % 2 == 0:
							plant(Entities.Carrot)
						else:
							plant(Entities.Tree)
			else:
				harvest()
				if i % 2 == 0:
					if n % 2 == 0:
						plant(Entities.Carrot)
					else:
						plant(Entities.Tree)
			move(North)
		move(East)