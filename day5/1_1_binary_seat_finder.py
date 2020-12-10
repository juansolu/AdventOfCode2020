import math

def get_seat_row(seats, example_boarding_pass):
    for direction in example_boarding_pass:
        curr_len = len(seats)
        keep_index = math.floor(curr_len / 2)
        #print(f"Pass action={direction} attempt to find keep_index={keep_index} currLen={curr_len}")
        if direction == 'F':
            del seats[keep_index:]
            #print(f"Taking lower half keeping seats {seats[0]} through to {seats[-1]}")
        elif direction == 'B':
            del seats[:keep_index]
            #print(f"Taking upper half keeping seats {seats[0]} through to {seats[-1]}")
        if seats[0] == seats[-1]:
            return seats[0]

    return seats[0]

def get_seat_col(seats, example_boarding_pass):
    for direction in example_boarding_pass:
        curr_len = len(seats)
        keep_index = math.floor(curr_len / 2)
        #print(f"Pass action={direction} attempt to find keep_index={keep_index} currLen={curr_len}")
        if direction == 'L':
            del seats[keep_index:]
            #print(f"Taking lower half keeping seats {seats[0]} through to {seats[-1]}")
        elif direction == 'R':
            del seats[:keep_index]
            #print(f"Taking upper half keeping seats {seats[0]} through to {seats[-1]}")
        if seats[0] == seats[-1]:
            return seats[0]

    return seats[0]

total_seat_count = 128
seat_col_option = 8

# FBFBBFFRLR: row 44, column 5, seat ID 357.
possible_row_list = list(range(0, total_seat_count))
possible_col_list = list(range(0, seat_col_option))
example_boarding_pass = "FBFBBFFRLR"
seat_row = get_seat_row(possible_row_list, example_boarding_pass)
seat_col = get_seat_col(possible_col_list, example_boarding_pass)
seat_id = seat_row * seat_col_option + seat_col
print(f"{example_boarding_pass} seat_row={seat_row} seat_col={seat_col} seat_id={seat_id}")

# BFFFBBFRRR: row 70, column 7, seat ID 567.
possible_row_list = list(range(0, total_seat_count))
possible_col_list = list(range(0, seat_col_option))
example_boarding_pass = "BFFFBBFRRR"
seat_row = get_seat_row(possible_row_list, example_boarding_pass)
seat_col = get_seat_col(possible_col_list, example_boarding_pass)
seat_id = seat_row * seat_col_option + seat_col
print(f"{example_boarding_pass} seat_row={seat_row} seat_col={seat_col} seat_id={seat_id}")

# FFFBBBFRRR: row 14, column 7, seat ID 119.
possible_row_list = list(range(0, total_seat_count))
possible_col_list = list(range(0, seat_col_option))
example_boarding_pass = "FFFBBBFRRR"

seat_row = get_seat_row(possible_row_list, example_boarding_pass)
seat_col = get_seat_col(possible_col_list, example_boarding_pass)
seat_id = seat_row * seat_col_option + seat_col
print(f"{example_boarding_pass} seat_row={seat_row} seat_col={seat_col} seat_id={seat_id}")

# BBFFBBFRLL: row 102, column 4, seat ID 820.
possible_row_list = list(range(0, total_seat_count))
possible_col_list = list(range(0, seat_col_option))
example_boarding_pass = "BBFFBBFRLL"

seat_row = get_seat_row(possible_row_list, example_boarding_pass)
seat_col = get_seat_col(possible_col_list, example_boarding_pass)
seat_id = seat_row * seat_col_option + seat_col
print(f"{example_boarding_pass} seat_row={seat_row} seat_col={seat_col} seat_id={seat_id}")

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
boarding_passes = [x.strip() for x in my_file.readlines()]

highest_seat_id = 0
for boarding_pass in boarding_passes:
    possible_row_list = list(range(0, total_seat_count))
    possible_col_list = list(range(0, seat_col_option))

    seat_row = get_seat_row(possible_row_list, boarding_pass)
    seat_col = get_seat_col(possible_col_list, boarding_pass)
    seat_id = seat_row * seat_col_option + seat_col
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

end_time = time.monotonic() - start_time

print(f"Highest seat id found in boarding passes={highest_seat_id}")