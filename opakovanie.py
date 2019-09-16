import sys
import csv
import statistics

data = []
file = sys.argv[1]

with open(file,'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        for e in row:
            data.append(int(e))


_min = min(data)
_max = max(data)
_len = len(data)
_mean = statistics.mean(data)
_median = statistics.median(data)

print(f"minimum: {_min}")
print(f"maximum: {_max}")
print(f"dlzka: {_len}")
print(f"priemer: {_mean}")
print(f"median: {_median}")

positive =[x for x in data if x > 0]
negative = [x for x in data if x < 0]

print(positive)
print(negative)

