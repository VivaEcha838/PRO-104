import csv

with open('SOCR-HeightWeight.csv', newline= '') as f:
    readfile = csv.reader(f)
    file_data = list(readfile)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    weight = file_data [i][2]
    new_data.append(float(weight))

n = len(new_data)
total = 0

for x in new_data:
    total = total + x

mean = total/n
print('Mean is :' + str(mean))
