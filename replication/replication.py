import utils
import subprocess
import params

cantor = params.CANTOR
depth_range = params.DEPTH_RANGE
width_range = params.WIDTH_RANGE
iterations = params.ITERATIONS

f = open(params.TRAINING_CSV, 'w')
f.write("0-homology, 1-homology, seed, depth, width, iteration\n")
f.close()
for x in utils.cantor(cantor):
    for depth in range(depth_range[0], depth_range[1]):
        for width in range(width_range[0], width_range[1]):
            for k in range(iterations):
                subprocess.call(['python3', 'replication_sub.py', str(
                    x[0]), str(x[1]), str(depth), str(width), str(k)])
