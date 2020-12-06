def get_value_match(entries, desired_sum):
    for first_value in entries:
        for second_value in entries:
            if first_value + second_value == desired_sum:
                return  first_value, second_value

    return 0, 0

entries = [1721, 979, 366, 299, 675, 1456]

desired_sum = 2020

first_entry, second_entry = get_value_match(entries, desired_sum)
print("desired_sum={} first_entry={} second_entry={}".format(desired_sum, first_entry, second_entry))
print("Multiplied total={}".format(first_entry * second_entry))

import time
start_time = time.monotonic()

#Acutally test with input data
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

print("-> Find data based on input.txt")
first_entry, second_entry = get_value_match(entries, desired_sum)
end_time = time.monotonic() - start_time

print("desired_sum={} first_entry={} second_entry={}".format(desired_sum, first_entry, second_entry))
print("Multiplied total={}".format(first_entry * second_entry))
print("Total time={}".format(end_time))
