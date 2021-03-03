import csv
import subprocess
import sys

training_file_path = '../models/training.csv'
evaluation_file = '../models/evaluation.csv'

index_start = 0
if len(sys.argv) > 1:
    index_start = int(sys.argv[1])

if index_start == 0:
    f = open(evaluation_file, 'w')
    f.write("0-homology, 1-homology, seed, depth, width, iteration, original_betti-0, original_betti-1, network_betti-0, network_betti-1, paper_original_eval_0, paper_computed_eval_0 , new_original_eval_0, new_computed_eval_0, paper_original_eval_1, paper_computed_eval_1 , new_original_eval_1, new_computed_eval_1\n")
    f.close()

with open(training_file_path, newline='\n') as f:
    reader = csv.reader(f)
    next(reader, None)
    for _ in range(index_start - 1):
        next(reader, None)

    for row in reader:
        subprocess.call(['python3', 'evaluate_betti_sub.py',
                         row[0], row[1], row[2], row[3], row[4], row[5]])
