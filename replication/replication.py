import utils
import subprocess

f = open('../models/training.csv', 'w')
f.write("0-homology, 1-homology, seed, depth, width, iteration\n")
f.close()
for x in utils.cantor(30):
    for depth in range(1, 5):
        for width in range(1, 15):
            for k in range(50):
                subprocess.call(['python3', 'replication_sub.py', str(
                    x[0]), str(x[1]), str(depth), str(width), str(k)])
