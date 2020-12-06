# Problem: Improve efficency through sorting first

def get_value_match(entries, desired_sum):
    for first_value in entries:
        for second_value in entries:
            for third_value in entries:
                if first_value + second_value + third_value == desired_sum:
                    return  first_value, second_value, third_value

    return 0, 0, 0


desired_sum = 2020

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
#optimization #1: if greater than desired_sum do not include in potential solution
entries = [int(x.strip()) for x in my_file.readlines() if int(x.strip()) < desired_sum]
#optimization #2:  see if sorting entries helps find match faster
#seems to work based on specific input
entries.sort()

print("Find desired total based on input.txt, entries length={}".format(len(entries)))
first_entry, second_entry, third_entry = get_value_match(entries, desired_sum)
end_time = time.monotonic() - start_time

print("desired_sum={} first_entry={} second_entry={}, third_entry={}".format(desired_sum, first_entry, second_entry, third_entry))
print("Multiplied total={}".format(first_entry * second_entry * third_entry))
print("Total time={}".format(end_time))
