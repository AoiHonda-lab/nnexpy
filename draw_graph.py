import csv
import matplotlib.pyplot as plt
import numpy as np

CSV_PATH = "/media/alexandre/0C83-6F0E/transfer/models/evaluation.csv" 
'''
with open(CSV_PATH, newline='\n') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        print(row[10], row[11], row[12], row[13])
'''


def create_table(index1, index2, index3):
    res = []
    iteration = []
    min1 = 100
    max1 = 0
    min2 = 100
    max2 = 0
    with open(CSV_PATH, newline='\n') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            r1 = int(row[index1])
            r2 = int(row[index2])
            r3 = float(row[index3])
            if min1 > r1 - 0.5:
                min1 = r1 - 0.5
            if max1 < r1 + 0.5:
                max1 = r1 + 0.5
            if min2 > r2 - 0.5:
                min2 = r2 - 0.5
            if max2 < r2 + 0.5:
                max2 = r2 + 0.5
            if len(res) < r1 + 1:
                for _ in range(r1 - len(res) + 1):
                    res.append([])
                    iteration.append([])
            if len(res[r1]) < r2 + 1:
                for _ in range(r2 - len(res[r1]) + 1):
                    res[r1].append(0)
                    iteration[r1].append(0)
            res[r1][r2] += r3
            iteration[r1][r2] += 1
        return np.arange(min1, max1 + 1, 1), np.arange(min2, max2 + 2, 1), res, iteration


x, y, Z, iteration = create_table(0, 4, 12)
for i in range(len(Z)):
    for j in range(len(Z[i])):
        if iteration[i][j] != 0:
            Z[i][j] /= iteration[i][j]

fig, ax = plt.subplots()
im = ax.pcolormesh(y, x, Z)
fig.colorbar(im, ax=ax)
plt.show()
