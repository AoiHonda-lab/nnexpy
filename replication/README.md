# Replication

## [`datasets_generation.py`](datasets_generation.py)

 [`datasets_generation.py`](datasets_generation.py) contains the functions to generate the datasets with given homology. It overwrites the original constructor of `DataDescriptor` by directly generating a `centerList` and a `radiusList`.   
 
 ```python3
 create_data_descriptor(threshold=0.05, minStrataThickness=0.9*threshold, strataDensity=0.2, dimension=2, dimensionDistribution=[0,...,0,1], maxUnsuccessfulAttempts=1000, seed=None):
    return nnexpy_min.DataDescriptor
 ```
 
 generates a `DataDescriptor` with the homology given by `dimensionDistribution`. `threshold` gives the gap mandatory between any two homologies. `minStrataThickness`, the thickness of the homologies (at least 1-homologies). `strataDensity` is the probability to generate (if possible) an homology around the lat homology creating another strata around it. `dimension` replace `dimensionDistribution` in the case where only one `dimension`-homology is required. Since the procedure is random, we can run in cases where there is no (or very little) places to put the remaining homologies, `maxUnsuccessfulAttempts` gives the number of unsuccessful tries to consecutively chose a random center that respects the chosen threshold in regards to the previously chosen center, strata and borders. In case this number is reach, the execution will `raise Exception("Unable to generate all the points, try with a smaller threshold")`
 
 ---------
 
 ```python3
 generate_descriptor(homology, threshold=0.05, threshold_decay=0.01, seed=None):
    return (nnexpy_min.DataDescriptor, threshold)
 ```
 
 generates a `DataDescriptor` using `create_data_descriptor` with `threshold` as the starting threshold and reducing the threshold by `threshold_decay` each time the execution fails due to unsuccessful center placement. It returns the `DataDescriptor` generated as well as the `threshold` of successful generation.
 
 
 ## [Training phase](replication.py)
 
 The training phase generates networks according to the chosen parameters (refer to `NetworkGenrator` doc as swell as the original article for more information). The training is done using `subprocess` to ensure that memory will be freed at the end of each network training. 
 
 ## [Evaluation phase](evaluate_betti.py)
 
 The evaluation phase uses [`gudhi`](http://gudhi.gforge.inria.fr/) to compute homologies (refer to `DataInstance` documentation for more details). We use `subprocess` to ensure that the memory is freed each time.
 
 
## [Parameters](params.py)

* `CANTOR` represents the list of continuously generated homology from `[1,0]` to `[CANTOR, CANTOR]`. The list is in the order given by the cantor polynomial.

* `DEPTH_RANGE` represents the depths of the networks trained during the training phase. According to python convention the upper bound is excluded.

* `WIDTH_RANGE` represents the width of the first hidden layer of the network trained during the training phase. According to python convention the upper bound is excluded.

* `ITERATIONS` is the number of time a same architecture (`DEPTH` and `WIDTH`) will be trained on a given homology.

The number of networks trained in the end will be `((CANTOR + 1)^2 - 1) x (DEPTH_RANGE[1] - DEPTH_RANGE[0]) x (WIDTH_RANGE[1] - WIDTH_RANGE[0]) x ITERATIONS`. For the default parameters it means 5,376,000 networks.

* `MODELS_FOLDER`: Path to store models (linux style, must end with `/`)

* `TRAINING_CSV`: Path to store training information

* `EVALUATION_CSV`: Path to store evaluation information


To do a full replication, you first need to copy `nnexpy_min` to the `replication` folder. After configuring `params.py` to your liking (most likely computation capacities), you need to run `replication.py`. Once `replication.py`'s run is over or during the run you can run `evaluation_betti.py`. I will compute the betti numbers for the results already written in `TRAINING_CSV`. `evaluation_betti` can be given a runtime parameter to chose the line of `TRAINING_CSV` it will start to read from. If none is given, `evaluation_betti` will start from 0 and overwrite `EVALUATION_CSV` otherwise it will append to it.  

Typically you would have to run these commands on `bash`:

```shell
cp -r nnexpy_min replication
conda env create -f environment.yml
conda activate nnexpy_min
cd replication
python3 replication.py
python3 evaluate_betti.py 0
```
