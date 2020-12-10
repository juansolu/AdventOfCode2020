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

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
boarding_passes = [x.strip() for x in my_file.readlines()]

seat_inventory = []
for boarding_pass in boarding_passes:
    possible_row_list = list(range(0, total_seat_count))
    possible_col_list = list(range(0, seat_col_option))

    seat_row = get_seat_row(possible_row_list, boarding_pass)
    seat_col = get_seat_col(possible_col_list, boarding_pass)
    seat_id = seat_row * seat_col_option + seat_col
    seat_inventory.append(seat_id)

seat_inventory.sort()

missing_id = 14
for seat_id in seat_inventory:
    if seat_id != missing_id +1:
        print(f"Expected seat={seat_id}")
    missing_id = seat_id

end_time = time.monotonic() - start_time
print(f"Found seats={seat_inventory}")
print(f"Time to execute={end_time}")
