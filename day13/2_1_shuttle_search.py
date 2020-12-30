import time
import sys
from functools import reduce

#https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n:list, a:list):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a: int, b:int):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_shuttle_bus_time_in_sequence(entries):
    #convert out of our array data fields we care about
    available_buses = entries[1][0].split(",")

    bus_ids = [int(v) for v in available_buses if not v == "x"]

    # For example, let's consider data = ["939", "7,13,x,x,59,x,31,19"]
    # Bus ids 7,13,59,31,19 have indexes 0,1,4,6,7 respectively. The indexes
    # represent the offset of the departures

    # Credit: https://github.com/bsounak/Aoc2020/blob/main/day13.py
    # We need to find the smallest T, such that
    # T % 7 is 0, which is 7-0
    # T % 13 is 12, which is 13-1
    # T % 59 is 55, which is 59-4
    # T % 31 is 25, which is 31-6
    # T % 19 is 12, which is 19-7
    bus_indexes = []
    for index, bus_id in enumerate(available_buses):
        if not bus_id == "x":
            bus_indexes.append(int(bus_id) - index)

    return chinese_remainder(bus_ids, bus_indexes)

entries = None

n = [3, 5, 7]
a = [2, 3, 2]
sol = chinese_remainder(n, a)
assert 23 == sol

n = [7, 13, 59, 31, 19]
a = [7, 12, 55, 25, 12]
sol = chinese_remainder(n, a)
assert 1068781 == sol

start_time = time.monotonic()
with open("input.txt", 'r') as file:
    entries = [x.split() for x in file.readlines()]

bus_earliest_leave_time = find_shuttle_bus_time_in_sequence(entries)

end_time = time.monotonic() - start_time
print(f"Found answer={bus_earliest_leave_time}")
print(f"Duration to complete={end_time}")