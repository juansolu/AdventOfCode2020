def traverse_terrain_with_slope(slope_tuple, terrain):
    terrain_column_location = 0
    num_trees_found = 0
    for rows_index, row in enumerate(terrain, start=0):
        if (rows_index == 0):
            continue
        terrain_column_location += slope_tuple[0] + slope_tuple[1] - 1
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

print(terrain_input)
slope_tuple = (3, 1)
print(slope_tuple)

count_trees = traverse_terrain_with_slope(slope_tuple, terrain_input)
print("Found terrain traverse tree count={}".format(count_trees))

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
terrain = [x.strip() for x in my_file.readlines()]
count_trees = traverse_terrain_with_slope(slope_tuple, terrain)
end_time = time.monotonic() - start_time

print("Found trees encountered count={}".format(count_trees))
print("Time={}".format(end_time))