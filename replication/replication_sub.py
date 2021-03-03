import datasets_generation
import random as r
import nnexpy_min
import os
import sys
import gc
import tensorflow as tf

x = [int(sys.argv[1]), int(sys.argv[2])]
depth = int(sys.argv[3])
width = int(sys.argv[4])
k = int(sys.argv[5])

seed = r.randint(0, 1000000)
print('')
print('==========================================')
print('')
print('HOMOLOGY= ', x, " DEPTH = ", depth,
      " WIDTH = ", width, " ITERATION = ", k)
print('')
print('==========================================')
print('')
descriptor, threshold = datasets_generation.generate_descriptor(
    x, seed=seed)
instance = descriptor.generateDataAlt(nPoints=5000, seed=seed)
data, label = instance.numpyify()
if not os.path.isdir('../models/' + str(x[0]) + '_' + str(x[1])):
    os.mkdir('../models/' + str(x[0]) + '_' + str(x[1]))
nnexpy_min.NetworkGenerator().full_net_combined(
    depth, depth, width, k, (2,), '../models/' + str(x[0]) + '_' + str(x[1]) + '/', 10000, max(x[0], 1), data, label)
f = open('../models/training.csv', 'a')
f.write(str(x[0]) + ',' + str(x[1]) + ',' + str(seed) + ',' +
        str(depth) + ',' + str(width) + ',' + str(k) + '\n')
f.close()

gc.collect()
tf.keras.backend.clear_session()
tf.compat.v1.reset_default_graph()
