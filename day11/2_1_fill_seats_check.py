import time
import copy

right_direction = (0,1)
behind_right_direction = (1, 1)
behind_direction = (1, 0)
behind_left_direction = (1,-1)
left_direction = (0, -1)
front_left_direction = (-1, -1)
front_direction = (-1,0)
front_right_direction = (-1, 1)


def find_seat_in_direction(seat_layout, row_index, col_index, target, direction):
    traverse_seat = True

    #some business logic to know we need to shortcircuit our searching because a non target seat state exists
    opposite_find = None
    if target == '#':
        opposite_find = 'L'
    else:
        opposite_find = '#'

    while traverse_seat:
        row_index += direction[0]
        col_index += direction[1]
        if row_index >= len(seat_layout) or col_index >= len(seat_layout[row_index]):
            traverse_seat = False
            break
        if row_index < 0 or col_index < 0:
            traverse_seat = False
            break
        if seat_layout[row_index][col_index] == opposite_find:
            return False
        elif seat_layout[row_index][col_index] == target:
            return True

    return False

def find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, target):
    seats_taken = 0

    #check seat to the right
    if find_seat_in_direction(seat_layout, row_index, col_index, target, right_direction):
        seats_taken += 1

    #check seats behind me
    if row_index + 1 < len(seat_layout):
        #check seat behind me on the right
        if find_seat_in_direction(seat_layout, row_index, col_index, target, behind_right_direction):
            seats_taken += 1

        #check seat directly behind me
        if find_seat_in_direction(seat_layout, row_index, col_index, target, behind_direction):
            seats_taken += 1

        #check seat behind me on the left
        if find_seat_in_direction(seat_layout, row_index, col_index, target, behind_left_direction):
            seats_taken += 1

    #check seat to my left
    if find_seat_in_direction(seat_layout, row_index, col_index, target, left_direction):
        seats_taken += 1

    if row_index > 0:
        #check seat in front of me to the left
        if col_index > 0 and find_seat_in_direction(seat_layout, row_index, col_index, target, front_left_direction):
            seats_taken += 1

        #check seat directly in front of me
        if find_seat_in_direction(seat_layout, row_index, col_index, target, front_direction):
            seats_taken += 1

        #check seat in front of me to the right
        if find_seat_in_direction(seat_layout, row_index, col_index, target, front_right_direction):
            seats_taken += 1

    return seats_taken

def check_if_should_take_seat(seat_layout, row_index, col_index):
    seat_count = find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, '#')
    if seat_count == 0:
        return True

    return False

def check_if_should_vacate_seat(seat_layout, row_index, col_index):
    seat_count = find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, '#')
    if seat_count >= 5:
        return True
    return False

def create_2d_seat_layout(entries):
    seat_layout = []
    for row in entries:
        seat_cols = []
        for col in row:
            seat_cols.append(col)
        seat_layout.append(seat_cols)
    return seat_layout

def find_seat_layout(entries):
    seat_layout = []
    for row in entries:
        seat_cols = []
        for col in row:
            seat_cols.append(col)
        seat_layout.append(seat_cols)

    iterations_count = 0
    previous_seats = None
    seats_changed = True
    while seats_changed:

        seat_layout_freeze = copy.deepcopy(seat_layout)
        for row_index, row in enumerate(seat_layout):
            for col_index, col in enumerate(row):
                if col == ".":
                    continue
                elif col == "L":
                    if check_if_should_take_seat(seat_layout_freeze, row_index, col_index):
                        seat_layout[row_index][col_index] = "#"
                elif col == "#":
                    if check_if_should_vacate_seat(seat_layout_freeze, row_index, col_index):
                        seat_layout[row_index][col_index] = "L"

        if previous_seats:
            seats_changed = False
            for row_index, row in enumerate(previous_seats):
                for col_index, col in enumerate(row):
                    if seat_layout[row_index][col_index] != col:
                        seats_changed = True

        iterations_count += 1
        previous_seats = copy.deepcopy(seat_layout)
        # for seats in seat_layout:
        #     print(f"Seating outcum iter={iterations_count}:{seats}")
        # print("")

    return seat_layout

entries = None

with open('test_scenario_8_occupied.txt', 'r') as file:  # Use file to refer to the file object
    entries = [x.strip() for x in file.readlines()]
seat_count = find_adjacent_seats_that_match_target(create_2d_seat_layout(entries), 4, 3, '#')
assert 8 == seat_count

with open('test_scenario_one_empty_seat.txt', 'r') as file:  # Use file to refer to the file object
    entries = [x.strip() for x in file.readlines()]
empty_seat_count = find_adjacent_seats_that_match_target(create_2d_seat_layout(entries), 1, 1, 'L')
assert 1 == empty_seat_count

with open('test_scenario_no_occupied.txt', 'r') as file:  # Use file to refer to the file object
    entries = [x.strip() for x in file.readlines()]
occupied_seat_count = find_adjacent_seats_that_match_target(create_2d_seat_layout(entries), 3, 3, '#')
assert 0 == occupied_seat_count

start_time = time.monotonic()
with open('input.txt', 'r') as file:  # Use file to refer to the file object
    entries = [x.strip() for x in file.readlines()]

seat_layout_result = find_seat_layout(entries)
print(f"Found seatlayout={seat_layout_result}")

count_seats_taken = sum([x.count('#') for x in seat_layout_result])
end_time = time.monotonic() - start_time
print(f"Answer={count_seats_taken}")
print(f"Time to execute={end_time}")
