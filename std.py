import csv

with open("data.csv", newline='') as f:
     reader = csv.reader(f)
     file_data = list(reader)

data=file_data[0]

# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)
    mean = total / n
    return mean

square_list = []
for i in data:
    a = int (i) - mean(data)
    a = a ** 2 # 3**2
    square_list.append(a)

sum = 0
for i in square_list:
     # sum = sum + i
    sum += i

result = sum/ (len(data)-1)

import math
std_dev = math.sqrt(result)
print(std_dev)
print("\n")


d = [60,61,65,63,98,99,90,95,91,96]
import statistics
std_dev2 = statistics.stdev( d )
print(std_dev2)