import time
import sys

def get_bus_depart_time_for_earliest_time(buses_available, earliest_time):
    buses_dict = {}
    min_wait_time = sys.maxsize
    buses = [int(bus) for bus in buses_available.split(",") if bus != 'x']
    buses.sort()

    bus_id_min = 0
    bus_wait_time = 0

    import pdb
    pdb.set_trace()
    for bus_id in buses:
        # assume bus_id is smaller than our expected earliest time
        modulo_to_earliest_time = earliest_time % bus_id
        next_bus_arrival = earliest_time + modulo_to_earliest_time
        time_spent_waiting_for_bus = 0
        if modulo_to_earliest_time != 0:
            time_spent_waiting_for_bus = bus_id - modulo_to_earliest_time
            next_bus_arrival = earliest_time + time_spent_waiting_for_bus

        if next_bus_arrival < min_wait_time:
            bus_wait_time = time_spent_waiting_for_bus
            bus_id_min = bus_id
            min_wait_time = next_bus_arrival

    return bus_id_min * bus_wait_time

def find_shuttle_bus_wait_time(entries):
    #convert out of our array data fields we care about
    earliest_time = int(entries[0][0])
    available_buses = entries[1][0]

    return get_bus_depart_time_for_earliest_time(available_buses, earliest_time)

entries = None

start_time = time.monotonic()
with open("input.txt", 'r') as file:
    entries = [x.split() for x in file.readlines()]

bus_wait_time = find_shuttle_bus_wait_time(entries)

end_time = time.monotonic() - start_time
print(f"Found answer={bus_wait_time}")
print(f"Duration to complete={end_time}")