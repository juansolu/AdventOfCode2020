def traverse_terrain_with_slope(slope_tuple, terrain):
    terrain_column_location = 0
    num_trees_found = 0
    slope_down_travel = 0
    print("** Start Traverse terrain with slope tuple right={}, down={}".format(slope_tuple[0], slope_tuple[1]))
    for rows_index, row in enumerate(terrain, start=0):
        # for when we go down multiple rows
        if slope_down_travel < slope_tuple[1]:
            slope_down_travel += 1
            print("skipping row index={} due to slope down travel value={}".format(rows_index, slope_down_travel))
            continue
        else:
            # reset how many times we travel down the slope
            slope_down_travel = 1

        terrain_column_location += slope_tuple[0]
        column_location_relative = (terrain_column_location % len(row))
        print("column location for row based on terrain_clumn_location={} with column_location={} row length={}".format(
            terrain_column_location, column_location_relative, len(row)
        ))
        is_tree_at_location = row[column_location_relative] == '#'
        print("Current terrain row location={} column location={} is tree at location={} row={}".format(
            rows_index, column_location_relative, is_tree_at_location, row))
        if is_tree_at_location:
            num_trees_found += 1

    return num_trees_found

terrain_input = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#']
trees_count_found_list = []

slope_tuples = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slope_tuples:
    count_trees = traverse_terrain_with_slope(slope, terrain_input)
    trees_count_found_list.append(count_trees)

import math
product_of_counted_tress = math.prod(trees_count_found_list)
print("Found terrain traverse tree count={} with multipled total={}".format(trees_count_found_list, product_of_counted_tress))

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
terrain = [x.strip() for x in my_file.readlines()]

trees_count_found_list.clear()

for slope in slope_tuples:
    count_trees = traverse_terrain_with_slope(slope, terrain)
    trees_count_found_list.append(count_trees)
end_time = time.monotonic() - start_time

product_of_counted_tress = math.prod(trees_count_found_list)
print("Found terrain traverse tree count={} with multipled total={}".format(trees_count_found_list, product_of_counted_tress))
print("Time={}".format(end_time))