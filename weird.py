while True:
	for i in range(get_world_size()):
		for n in range(get_world_size()):
			if i % 3 == 1 and n % 2 == 1:
				use_item(Items.Weird_Substance)
			harvest()
			move(North)
		move(East)