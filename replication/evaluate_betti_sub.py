from tensorflow import keras
import nnexpy_min
import datasets_generation
from sys import argv

models_directory = "../models/"
evaluation_file = "../models/evaluation.csv"

homology = [int(argv[1]), int(argv[2])]
seed = int(argv[3])
model = keras.models.load_model(
    models_directory + argv[1] + '_' + argv[2] + '/' + argv[4] + '_' + argv[5] + '_' + argv[6] + '.h5')
descriptor, threshold = datasets_generation.generate_descriptor(
    homology, seed=seed)
instance = descriptor.generateDataAlt(nPoints=10000, seed=seed)
originalBetti = instance.bettiNumbers(threshold=threshold)
networkInstance = instance.predict(
    model)
networkBetti = networkInstance.bettiNumbers(threshold=threshold/2)

paper_original_eval = [min(1, max(1, networkBetti[0])/max(1, homology[0])),
                       min(1, max(1, networkBetti[1])/max(1, homology[1]))]
new_original_eval = [min(max(1, homology[0])/max(1, networkBetti[0]), max(1, networkBetti[0])/max(1, homology[0])),
                     min(max(1, homology[1])/max(1, networkBetti[1]), max(1, networkBetti[1])/max(1, homology[1]))]
paper_computed_eval = [min(1, max(1, networkBetti[0])/max(1, originalBetti[0])),
                       min(1, max(1, networkBetti[1])/max(1, originalBetti[1]))]
new_computed_eval = [min(max(1, originalBetti[0])/max(1, networkBetti[0]), max(1, networkBetti[0])/max(1, originalBetti[0])),
                     min(max(1, originalBetti[1])/max(1, networkBetti[1]), max(1, networkBetti[1])/max(1, originalBetti[1]))]
f = open(evaluation_file, 'a')
f.write(argv[1] + ',' + argv[2] + ',' + argv[3] + ',' + argv[4] + ',' + argv[5] + ',' + argv[6] + ',' + str(originalBetti[0]) + ',' + str(originalBetti[1]) + ',' + str(networkBetti[0]) + ',' + str(networkBetti[1]) + ',' + str(paper_original_eval[0]) + ',' + str(paper_computed_eval[0]) + ',' + str(new_original_eval[0]
                                                                                                                                                                                                                                                                                                          ) + ',' + str(new_computed_eval[0]) + ',' + str(paper_original_eval[1]) + ',' + str(paper_computed_eval[1]) + ',' + str(new_original_eval[1]) + ',' + str(new_computed_eval[1]) + '\n')
f.close()
