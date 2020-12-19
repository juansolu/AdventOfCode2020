import re
import pprint


def create_full_bag_inventory_lookup(entries):
    bag_token_map = {}
    for entry in entries:
        new_bag_fit_id = entry[:entry.index("bags")].strip()
        if new_bag_fit_id not in bag_token_map:
            numbers_data = re.findall('[0-9]+', entry)
            numbers = [int(i) for i in numbers_data]

            bag_token_map.update({
                new_bag_fit_id: get_referenced_bags_in_entry(entry)
                })

    pprint.pprint(bag_token_map)
    return bag_token_map

def get_referenced_bags_in_entry(entry):
    referenced_bags_in_entry = entry[(entry.index("contain")+7):]
    other_bags = referenced_bags_in_entry.split(",")
    referenced_bags = []
    for bags in other_bags:
        digit_matches = re.findall('[0-9]+', bags)
        num_bags = 0
        if digit_matches:
            # expect only one number in the bag token
            num_bags = int(digit_matches[0])

        bag_no_num = re.sub(r'[0-9]+', '', bags)
        # we assign the bag name as a list so we can use
        # math operands on the element to make more references for each bag name
        clean_bag_name_list = [bag_no_num.replace("bags", "").replace("bag", "").replace(".", "").strip()]

        if num_bags:
            referenced_bags += clean_bag_name_list * num_bags

    return referenced_bags


def find_bag_color_fit(bag_fit_id, bag_fit_lookup):
    if bag_fit_lookup.get(bag_fit_id) is None:
        return 0

    contained_bags = len(bag_fit_lookup[bag_fit_id])

    if not contained_bags:
        return 0

    contained_bags_cnt = len(bag_fit_lookup[bag_fit_id])
    total_child_counts = []
    for bag_name in bag_fit_lookup[bag_fit_id]:
        total_child_counts.append(find_bag_color_fit(bag_name, bag_fit_lookup))
    return sum(total_child_counts)+contained_bags_cnt

bag_token_find = "shiny gold"

import time
my_file = open("example.txt", "r")
entries = [x.strip() for x in my_file.readlines()]
bag_fit_lookup = create_full_bag_inventory_lookup(entries)
bags_for_color_results = find_bag_color_fit(bag_token_find, bag_fit_lookup)
assert 32 == bags_for_color_results

my_file = open("example_2.txt", "r")
entries = [x.strip() for x in my_file.readlines()]

bag_fit_lookup = create_full_bag_inventory_lookup(entries)
bags_for_color_results = find_bag_color_fit(bag_token_find, bag_fit_lookup)
assert 126 == bags_for_color_results

start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [x.strip() for x in my_file.readlines()]

bag_fit_lookup = create_full_bag_inventory_lookup(entries)
bags_for_color_results = find_bag_color_fit(bag_token_find, bag_fit_lookup)
end_time = time.monotonic() - start_time
print(f"Found answer count={bags_for_color_results}")
print(f"Time to execute={end_time}")