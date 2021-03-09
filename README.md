# NNexpy-min (A fork of NNexpy for the replication of the original experiment)

## Introduction

This repository is minimum version of [nnexpy](https://github.com/Spiilgriim/nnexpy). The purpose of this repository is to provide the minimal code to replicate the experiment that originally inspired part of my research. The article describing the original experiment can be found [here](https://arxiv.org/abs/1802.04443). 

## Requirement

To run this code you need python3 as well as some libraries. They can be installed using Conda and I personally used a conda environment which [environment file](environment.yml) is available in this repository.

To setup a functional conda environment with conda cli you simply need to use the following command:

```shell
conda env create -f environment.yml
conda activate nexpy
```

For more information refer to [conda documentation](https://docs.conda.io/projects/conda/en/latest/index.html) and in particular the section about [managing environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

## Usage

To use this code, copy the nnexpy_min folder in your python project (`replication` if you want to replicate the original experiment) and import `nnexpy_min`

```python
import nnexpy_min
```

NNexpy_min contains the following classes:

* [Bounds](docs/Bounds.md)
* [DataDescriptor](docs/DataDescriptor.md)
* [DataInstance](docs/DataInstance.md)
* [DataPoint](docs/DataPoint.md)
* [NetworkGenerator](docs/NetworkGenerator.md)

## Replication

For the purpose of replicating the original experiment, we provide some scripts in [`replication`](replication/). The parameters corresponding to the number of trained networks and the homology of the datasets on which they are trained can be chosen in [`params`](replication/params.py).
 
* `CANTOR` represents the list of continuously generated homology from `[1,0]` to `[CANTOR, CANTOR]`. The list is in the order given by the cantor polynomial.

* `DEPTH_RANGE` represents the depths of the networks trained during the training phase. According to python convention the upper bound is excluded.

* `WIDTH_RANGE` represents the width of the first hidden layer of the network trained during the training phase. According to python convention the upper bound is excluded.

* `ITERATIONS` is the number of time a same architecture (`DEPTH` and `WIDTH`) will be trained on a given homology.

The number of networks trained in the end will be `((CANTOR + 1)^2 - 1) x (DEPTH_RANGE[1] - DEPTH_RANGE[0]) x (WIDTH_RANGE[1] - WIDTH_RANGE[0]) x ITERATIONS`. For the default parameters it means 5,376,000 networks.

More information on the purpose of each script is available in [`replication`](replication/)
