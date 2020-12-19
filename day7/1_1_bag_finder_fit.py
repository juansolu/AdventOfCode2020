def create_full_inventory_index(entries):
    entries_list = []
    for entry in entries:
        new_bag_fit_id = entry[:entry.index("bags")]
        if new_bag_fit_id not in entries_list:
            entries_list.append(new_bag_fit_id)

    return entries_list

def find_bag_color_fit(entries, bag_fit_id):
    available_bag_fit = []
    bag_fit_ids = [bag_fit_id]
    bag_can_fit_bag = True

    while bag_can_fit_bag:
        bag_can_fit_bag = False
        for entry in entries:
            for bag_candidate in bag_fit_ids:
                if bag_candidate in entry:
                    new_bag_fit_id = entry[:entry.index("bags")].strip()
                    if new_bag_fit_id not in bag_fit_ids:
                        print(f"New id added={new_bag_fit_id}")
                        bag_fit_ids.append(new_bag_fit_id)
                        bag_can_fit_bag = True
                        break

    print(f"Available bags={bag_fit_ids}")
    return len(bag_fit_ids) - 1 # remove initial id bag

bag_token_find = "shiny gold"

import time
start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [x.strip() for x in my_file.readlines()]

num_bags_fit_count = find_bag_color_fit(entries, bag_token_find)
end_time = time.monotonic() - start_time

print(f"Found answer count={num_bags_fit_count}")
print(f"Time to execute={end_time}")