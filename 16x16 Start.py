def harvesting():
    for i in range(get_world_size()):
        harvest()
        move(North)

for i in range(get_world_size() - 1):
    spawn_drone(harvesting)
    move(East)
spawn_drone(harvesting)