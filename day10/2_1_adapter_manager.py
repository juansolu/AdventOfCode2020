import time

def has_valid_adapter_ranges(entries, max_diff):
    last_adapter_val = 0
    for voltage in entries:
        adapter_diff = voltage - last_adapter_val
        if adapter_diff > max_diff:
            return False
        last_adapter_val = voltage

    return True

def find_next_skippable_adapater_index(entries, next_index, max_diff):
    if next_index + 2 > len(entries):
        return 0
    import pdb
    pdb.set_trace()
    for removal_candidate in range(next_index, len(entries)):
        if entries[next_index + removal_candidate + 1] - entries[removal_candidate] < max_diff:
            return removal_candidate #skip the next element

    return 0

def find_adapter_arrangements(entries):
    linkers = {n: 1 for n in entries}
    for index, voltage in enumerate(entries):
        for next_index in (index+2, index+3):
            if next_index < len(entries) and entries[next_index] - voltage <= 3:
                for other_voltage in entries[next_index:]:
                    linkers[other_voltage] += linkers[voltage]
            else:
                #We check the next two numbers to see if the current number can be linked to the following number
                #Since we know the tuple jump is already more than 3 we don't need to check the other options
                break

    return linkers[max(entries)]

max_diff_voltage = 3

my_file = open("example.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]
entries.append(0)
entries.append(max(entries)+3)
entries.sort()
adapter_arrangements = find_adapter_arrangements(entries)
print(f"Found adapters={adapter_arrangements}")
assert adapter_arrangements == 8

print(f"Found answer count={adapter_arrangements}")

my_file = open("example2.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]
entries.append(0)
entries.append(max(entries)+3)
adapter_arrangements = find_adapter_arrangements(entries)
print(f"Found adapters={adapter_arrangements}")
assert adapter_arrangements == 19208

print(f"Found answer count={adapter_arrangements}")

start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]
entries.append(0)
entries.append(max(entries)+3)
entries.sort()
adapter_arrangements = find_adapter_arrangements(entries)
end_time = time.monotonic() - start_time

print(f"Found answer={adapter_arrangements}")
print(f"Time to execute={end_time}")