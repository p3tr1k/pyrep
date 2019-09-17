vals = (1,2,3,4,5)
print(vals[0])

print(f"there are {len(vals)} elements in tuple")

for e in vals:
    print(e)

print()
#***********************************************************
vals2 = [1,2,3,4,5]

vals2.append(6)
print(f"there are {len(vals)} elements in list")

for e in vals2:
    print(e)

print()
#*************************************************************
items = {"coins":5, "pens":8}

for k,v in items.items():
    print(k,v)

print()
#************************************************************

data = {1,2,3,4,5}
print(data)
