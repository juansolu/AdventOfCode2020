import time

def find_adapter_ranges(entries):
    adapter_diffs = {}
    entries.sort()
    print(f"Entries={entries}")
    last_adapter_val = 0
    for voltage in entries:
        adapter_diff = voltage - last_adapter_val
        if adapter_diff not in adapter_diffs:
            adapter_diffs[adapter_diff] = 1
        else:
            adapter_diffs[adapter_diff] += 1
        last_adapter_val = voltage

    #add the last built-in adapter difference from the highest value
    adapter_diffs[3] += 1

    return adapter_diffs

start_time = time.monotonic()
my_file = open("example.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

adapter_ranges = find_adapter_ranges(entries)
assert adapter_ranges[1] == 7
assert adapter_ranges[3] == 5

end_time = time.monotonic() - start_time

print(f"Found answer count={adapter_ranges}")
print(f"Time to execute={end_time}")

start_time = time.monotonic()
my_file = open("example2.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

adapter_ranges = find_adapter_ranges(entries)

assert adapter_ranges[1] == 22
assert adapter_ranges[3] == 10

end_time = time.monotonic() - start_time

print(f"Found answer count={adapter_ranges}")
print(f"Time to execute={end_time}")

start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [int(x.strip()) for x in my_file.readlines()]

adapter_ranges = find_adapter_ranges(entries)
voltage_total = adapter_ranges[1] * adapter_ranges[3]
end_time = time.monotonic() - start_time

print(f"Found voltage_diffs={adapter_ranges} answer={voltage_total}")
print(f"Time to execute={end_time}")