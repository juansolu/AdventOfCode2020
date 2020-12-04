# Problem:

# find three numbers in your expense report that meet the same criteria.

# Using the previous input again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

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

#Acutally test with input data
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

print("-> Find data based on input.txt")
first_entry, second_entry, third_entry = get_value_match(entries, desired_sum)
print("desired_sum={} first_entry={} second_entry={}, third_entry={}".format(desired_sum, first_entry, second_entry, third_entry))
print("Multiplied total={}".format(first_entry * second_entry * third_entry))

#Right answer: 199068980