import time

def get_preamble_sum_options(entries, preamble, offset_index):
    if len(entries) < preamble:
        return 0

    subset_we_care_about = entries[offset_index:offset_index+preamble]
    sum_for_preamble = {}
    for index, item in enumerate(subset_we_care_about):
        sum_for_preamble[item] = []
        reduced_subset = subset_we_care_about.copy()
        reduced_subset.pop(index)
        for sum_candidate in reduced_subset:
            sum_for_preamble[item].append(item + sum_candidate)

    return sum_for_preamble

def find_flaw_in_preamble(entries, preamble):
    flaw_in_preamble_sum = 0
    for index, entry in enumerate(entries):
        if flaw_in_preamble_sum != 0:
            return flaw_in_preamble_sum

        sum_for_preamble = get_preamble_sum_options(entries, preamble, index)
        validate_next_num_index = preamble + index

        if validate_next_num_index < len(entries):
            flaw_in_preamble_sum = entries[validate_next_num_index]
            print(f"Working on entry={entry} with valid ops={sum_for_preamble}")
            for key in sum_for_preamble:
                if flaw_in_preamble_sum in sum_for_preamble[key]:
                    flaw_in_preamble_sum = 0
                    break #we found a match in sum so this number isn't an issue

    return flaw_in_preamble_sum

#preamble = range of numbers that next number's sum is possibile for
#preamble = 5 # for example.txt
preamble = 25

start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

flawed_sum = find_flaw_in_preamble(entries, preamble)
end_time = time.monotonic() - start_time

print(f"Found answer count={flawed_sum}")
print(f"Time to execute={end_time}")