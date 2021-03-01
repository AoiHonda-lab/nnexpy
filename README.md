# NNexpy (A bunch of python script and classes to experiment with homology, knot theory and neural networks) 

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

To use this code, copy the nnexpy-min folder in your python project and import `nnexpy-min`

```python
import nnexpy-min
```

NNexpy contains the following classes:

* [Bounds](docs/Bounds.md)
* [DataDescriptor](docs/DataDescriptor.md)
* [DataInstance](docs/DataInstance.md)
* [DataPoint](docs/DataPoint.md)
* [NetworkGenerator](docs/NetworkGenerator.md)

## Replication

To replicate the original experiment multiple scripts have been created and can be found in [`replication`](replication/)
