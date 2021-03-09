# CANTOR represents the list of continuously generated homology from [1,0] to [CANTOR, CANTOR]. The list is in the order given by the cantor polynomial.
CANTOR = 30

# DEPTH_RANGE represents the depths of the networks trained during the training phase. According to python convention the upper bound is excluded.
DEPTH_RANGE = [1, 5]

# WIDTH_RANGE represents the width of the first hidden layer of the network trained during the training phase. According to python convention the upper bound is excluded.
WIDTH_RANGE = [1, 15]

# ITERATIONS is the number of time a same architecture (DEPTH and WIDTH) will be trained on a given homology.
ITERATIONS = 100

# The number of networks trained in the end will be ((CANTOR + 1)^2 - 1) x (DEPTH_RANGE[1] - DEPTH_RANGE[0]) x (WIDTH_RANGE[1] - WIDTH_RANGE[0]) x ITERATIONS. For the default parameters it means 5,376,000 networks.

# Path to store models (linux style, must end with /)
MODELS_FOLDER = '../models/'

# Path to store training information
TRAINING_CSV = '../models/training.csv'

# Path to store evaluation information
EVALUATION_CSV = '../models/evaluation.csv'
