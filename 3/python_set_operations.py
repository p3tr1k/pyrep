#!/usr/bin/python3

# set1 = { 'a', 'b', 'c', 'c', 'd' }
# set2 = { 'a', 'b', 'x', 'y', 'z' }

# print("Set 1:", set1)
# print("Set 2:", set2)
# print("intersection:", set1.intersection(set2))
# print("union:", set1.union(set2))
# print("difference:", set1.difference(set2))
# print("symmetric difference:", set1.symmetric_difference(set2))

# *************************************************************************

set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1 & set2)
print("union:", set1 | set2)
print("difference:", set1 - set2)
print("symmetric difference:", set1 ^ set2)