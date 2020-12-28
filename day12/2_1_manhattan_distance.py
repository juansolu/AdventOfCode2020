import time

class Waypoint(object):
    units = 0
    direction = 0

    def update_north_south_units(self, units_change):
        if self.direction == 0 or self.direction == 2:
            self.units += units_change

    def reflect_units_based_on_direction(self, past_direction):
        if past_direction in [2, 3] and self.direction in [0, 1]:
            self.units = self.units * -1
        elif past_direction in [0, 1] and self.direction in [2, 3]:
            self.units = self.units * -1

    def update_east_west_units(self, units_change):
        if self.direction == 1 or self.direction == 3:
            self.units += units_change

    def turn_right(self, degrees):
        directions_changed = int(degrees / 90)
        past_direction = self.direction
        self.direction = (self.direction + directions_changed) % 4
        self.reflect_units_based_on_direction(past_direction)

    def turn_left(self, degrees):
        directions_changed = int(degrees / 90)
        past_direction = self.direction
        self.direction = (self.direction + (-1*directions_changed)) % 4
        self.reflect_units_based_on_direction(past_direction)

def perform_action(north_south, east_west, waypoint_tuple, action):
    task = action[0]
    task_value = int(action[1:])
    if task == 'N':
        waypoint_tuple[0].update_north_south_units(task_value)
        waypoint_tuple[1].update_north_south_units(task_value)
    elif task == 'S':
        waypoint_tuple[0].update_north_south_units(-1*task_value)
        waypoint_tuple[1].update_north_south_units(-1*task_value)
    elif task == 'E':
        waypoint_tuple[0].update_east_west_units(task_value)
        waypoint_tuple[1].update_east_west_units(task_value)
    elif task == 'W':
        waypoint_tuple[0].update_east_west_units(-1*task_value)
        waypoint_tuple[1].update_east_west_units(-1*task_value)
    elif task == 'L':
        waypoint_tuple[0].turn_left(task_value)
        waypoint_tuple[1].turn_left(task_value)
    elif task == 'R':
        waypoint_tuple[0].turn_right(task_value)
        waypoint_tuple[1].turn_right(task_value)
    elif task == 'F':
        #move straight based on direction heading
        if waypoint_tuple[0].direction in [0,2]:
            north_south += waypoint_tuple[0].units * task_value
            east_west += waypoint_tuple[1].units * task_value
        else:
            north_south += waypoint_tuple[1].units * task_value
            east_west += waypoint_tuple[0].units * task_value

    return north_south, east_west

def find_manhattan_distance(entries):
    #initialize waypoint based on initial requirements
    waypoint1 = Waypoint()
    waypoint1.units = 10
    waypoint1.direction = 1
    waypoint2 = Waypoint()
    waypoint2.units = 1
    waypoint2.direction = 0
    waypoint = (waypoint1, waypoint2)

    north_south = 0
    east_west = 0

    for entry in entries:
        north_south, east_west = perform_action(north_south, east_west, waypoint, entry)

    return abs(north_south) + abs(east_west)

entries = None

start_time = time.monotonic()

with open("input.txt", "r") as file:
    entries = [x.strip() for x in file.readlines()]

total_distance = find_manhattan_distance(entries)
end_time = time.monotonic() - start_time

print(f"Answer={total_distance}")
print(f"Time={end_time}")