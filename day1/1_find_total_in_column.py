# Problem:

# The Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

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

#Acutally test with input data
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

print("-> Find data based on input.txt")
first_entry, second_entry = get_value_match(entries, desired_sum)
print("desired_sum={} first_entry={} second_entry={}".format(desired_sum, first_entry, second_entry))
print("Multiplied total={}".format(first_entry * second_entry))

#right answer: 786811