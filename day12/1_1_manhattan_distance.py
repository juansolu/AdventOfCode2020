import time

def perform_action(north_south, east_west, heading, action):

    if action[0] == 'N':
        north_south += int(action[1:])
    elif action[0] == 'S':
        north_south -= int(action[1:])
    elif action[0] == 'E':
        east_west += int(action[1:])
    elif action[0] == 'W':
        east_west -= int(action[1:])
    elif action[0] == 'L':
        degree_change = int(action[1:])
        directions_changed = int(degree_change / 90)
        heading = (heading + (-1*directions_changed)) % 4
    elif action[0] == 'R':
        degree_change = int(action[1:])
        directions_changed = int(degree_change / 90)
        heading = (heading + directions_changed) % 4
    elif action[0] == 'F':
        #move straight based on direction heading
        move_amount = int(action[1:])
        if heading == 0:
            north_south += move_amount
        elif heading == 1:
                east_west += move_amount
        elif heading == 2:
                north_south -= move_amount
        elif heading == 3:
                east_west -= move_amount

    return north_south, east_west, heading

def find_manhattan_distance(entries):
    north_south = 0
    east_west = 0

    #0=NORTH, 1=EAST, SOUTH=2, WEST=3
    heading = 1

    for entry in entries:
        north_south, east_west, heading = perform_action(north_south, east_west, heading, entry)

    print(f"Adding ns={north_south} + ew={east_west}")
    return abs(north_south) + abs(east_west)

entries = None

heading = 0
north_south, east_west, heading = perform_action(0, 0, heading, "R90")
assert heading == 1
north_south, east_west, heading = perform_action(0, 0, heading, "R90")
assert heading == 2
north_south, east_west, heading = perform_action(0, 0, heading, "R90")
assert heading == 3
north_south, east_west, heading = perform_action(0, 0, heading, "R90")
assert heading == 0

north_south, east_west, heading = perform_action(0, 0, heading, "R180")
assert heading == 2
north_south, east_west, heading = perform_action(0, 0, heading, "R180")
assert heading == 0

north_south, east_west, heading = perform_action(0, 0, heading, "R270")
assert heading == 3
north_south, east_west, heading = perform_action(0, 0, heading, "L270")
assert heading == 0



start_time = time.monotonic()

with open("input.txt", "r") as file:
    entries = [x.strip() for x in file.readlines()]

total_distance = find_manhattan_distance(entries)

end_time = time.monotonic() - start_time

print(f"Answer={total_distance}")
print(f"Time={end_time}")