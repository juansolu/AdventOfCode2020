import time
import re

def get_empty_bit_value():
    return [0] * 36

def get_sum_of_memory_address(memory_storage, index):
    binary_memory_string = ''.join(map(str, memory_storage[index]))
    return int(binary_memory_string, 2)

def update_memory_with_mask_applied(memory_storage, index_to_alter, mask_map, memory_value_override):
    #TODO: Something here seems to be wrong for when trying to apply masks on an already existing memory_storage index
    if len(memory_value_override) == 1 and memory_value_override[0] == 0:
        memory_value_override = get_empty_bit_value()
    len_bit_offset = len(memory_value_override)

    for index, value_to_apply in enumerate(memory_value_override):
        changed_bit_index = len(memory_storage[index_to_alter]) - len_bit_offset + index -1
        memory_storage[index_to_alter][changed_bit_index] = int(value_to_apply)


    for key in mask_map:
        memory_storage[index_to_alter][key] = mask_map[key]

    print(f"current memory={get_sum_of_memory_address(memory_storage, index_to_alter)}")
    return memory_storage

def get_mask_map_from_string(data):
    mask_map = {}
    mask_items = list(data)
    for index, entry in enumerate(mask_items):
        if entry != 'X':
            mask_map[index] = int(entry)
    #print(f"Mask map={mask_map}")
    return mask_map

def get_mask_sum_for_docking(entries):
    # expect entries format style to be of either:
    # 1-> mask = 1111011X01101X1XX100000000000X01X000
    # 2-> mem[8] = 11
    # significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right
    memory_storage = {}
    for entry in entries:
        if "mask" in entry:
            mask = entry.split("= ")[1]
            mask_map = get_mask_map_from_string(mask)
        else:
            index_to_alter = int(re.findall(r'\d+', entry.split(" =")[0])[0])
            mem_override_val_tens_scale = int(entry.split("= ")[1])
            #print(f"Memory value alteration={mask_alter_override_tuple}")

            if index_to_alter not in memory_storage:
                memory_storage[index_to_alter] = get_empty_bit_value()

            string_value_to_apply_from_binary = list("{0:b}".format(mem_override_val_tens_scale))
            memory_value_override = [int(i) for i in string_value_to_apply_from_binary]
            memory_storage = update_memory_with_mask_applied(memory_storage, index_to_alter, mask_map, memory_value_override)

    total_count = 0

    for key in memory_storage:
        total_count += get_sum_of_memory_address(memory_storage, key)

    return total_count

# TODO: Blocked on this solution as bitwise mask is not succeeding for the below scenario.
memory_storage = {}
target_index = 10149
string_value_to_apply_from_binary = list("{0:b}".format(59867532821))
memory_value_override = [int(i) for i in string_value_to_apply_from_binary]
memory_storage[target_index] = memory_value_override
mask_raw = "1111X011XXX010X0X100010000001001XX10"
mask_map = get_mask_map_from_string(mask_raw)
string_value_to_apply_from_binary = "{0:b}".format(2044502)
memory_value_override = [int(i) for i in string_value_to_apply_from_binary]
memory_storage = update_memory_with_mask_applied(memory_storage, target_index, mask_map, memory_value_override)
assert 65239007382 == get_sum_of_memory_address(memory_storage, target_index)

start_time = time.monotonic()

entries = None
with open("example.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]

mask_total_sum_values = get_mask_sum_for_docking(entries)

end_time = time.monotonic() - start_time
print(f"Answer={mask_total_sum_values}")
print(f"Execution duration={end_time}")