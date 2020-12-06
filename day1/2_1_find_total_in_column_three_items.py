def get_value_match(entries, desired_sum):
    for first_value in entries:
        for second_value in entries:
            for third_value in entries:
                if first_value + second_value + third_value == desired_sum:
                    return  first_value, second_value, third_value

    return 0, 0, 0

entries = [1721, 979, 366, 299, 675, 1456]

desired_sum = 2020

first_entry, second_entry, third_entry = get_value_match(entries, desired_sum)
print("desired_sum={} first_entry={} second_entry={} third_entry={}".format(desired_sum, first_entry, second_entry, third_entry))
print("Multiplied total={}".format(first_entry * second_entry * third_entry))

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

print("Find desired total based on input.txt, entries length={}".format(len(entries)))
first_entry, second_entry, third_entry = get_value_match(entries, desired_sum)
end_time = time.monotonic() - start_time

print("desired_sum={} first_entry={} second_entry={}, third_entry={}".format(desired_sum, first_entry, second_entry, third_entry))
print("Multiplied total={}".format(first_entry * second_entry * third_entry))
print("Total time={}".format(end_time))
