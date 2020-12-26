import time
import copy

def find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, target_for_switching):
    seats_taken = 0

    #check seat to the right
    if col_index + 1 < len(seat_layout[row_index]) and seat_layout[row_index][col_index+1] == target_for_switching:
        seats_taken += 1

    #check seats behind me
    if row_index + 1 < len(seat_layout):
        #check seat behind me on the right
        if col_index + 1 < len(seat_layout[row_index]) and seat_layout[row_index+1][col_index+1] == target_for_switching:
            seats_taken += 1

        #check seat directly behind me
        if seat_layout[row_index+1][col_index] == target_for_switching:
            seats_taken += 1

        #check seat behind me on the left
        if col_index > 0 and seat_layout[row_index+1][col_index-1] == target_for_switching:
            seats_taken += 1

    #check seat to my left
    if col_index > 0 and seat_layout[row_index][col_index-1] == target_for_switching:
        seats_taken += 1

    if row_index > 0:
        #check seat in front of me to the left
        if col_index > 0 and seat_layout[row_index-1][col_index-1] == target_for_switching:
            seats_taken += 1

        #check seat directly in front of me
        if seat_layout[row_index-1][col_index] == target_for_switching:
            seats_taken += 1

        #check seat in front of me to the right
        if col_index + 1 < len(seat_layout[row_index-1]) and seat_layout[row_index-1][col_index+1] == target_for_switching:
            seats_taken += 1

    return seats_taken

def check_if_should_take_seat(seat_layout, row_index, col_index):
    seat_count = find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, '#')
    if seat_count > 0:
        return False

    return True

def check_if_should_vacate_seat(seat_layout, row_index, col_index):
    seat_count = find_adjacent_seats_that_match_target(seat_layout, row_index, col_index, '#')
    if seat_count >= 4:
        return True
    return False

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

start_time = time.monotonic()
with open('input.txt', 'r') as file:  # Use file to refer to the file object
    entries = [x.strip() for x in file.readlines()]

seat_layout_result = find_seat_layout(entries)
print(f"Found seatlayout={seat_layout_result}")

count_seats_taken = sum([x.count('#') for x in seat_layout_result])
end_time = time.monotonic() - start_time
print(f"Answer={count_seats_taken}")
print(f"Time to execute={end_time}")
