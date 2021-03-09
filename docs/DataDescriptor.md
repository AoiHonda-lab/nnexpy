# DataDescriptor

Data Descriptor is an object used to store all information that caracterize a set of balls and spheres (or thick spheres)

## Class Variables

`dimension` (`int`): Dimension of the data. Corresponds to the dimension of the `Bounds` and `DataPoint` in `centerList` 

`bounds` (`Bounds`): Bounds of the data. 

`centerList` (`[DataPoint]`): Array containing the center points of the different homology in the data. Length corrsponds to `holeDimension` and `radiusList`'s length

`radiusList` (`[[(minRadius, maxRadius)]]`): Array containing the list of strata for each feature. Length corresponds to `holeDimension` and `centerList`'s length

`holeDimension` (`[int]`): Dimension of each homology. Length corresponds to `centerList` and `radiusList`'s length

## Constructors

```python
__init__(dimension=2, bounds=Bounds(dimension=2), radiusList=None, maxStrata=1, minStrata=1, random=None, nHoles=None, holeDimension=[2]*nHoles, orientation=[[]*nHoles])
```
Generate a `DataDescriptor` generating the missing information randomly with `random` as see if different from `None`

## Methods

```python
generateTestData(nPoints=1000):
  return DataInstance
```
Generates a `DataInstance` corresponding to the `DataDescriptor`'s `Bounds`  with only one class

---

```python
plot():
```
Plot the data instance if `dimension < 4`

---

```python
generateData(classNumber=2, nPoints=1000, random=None):
  return DataInstance
```
Generate a `DataInstance` with `classNumber` classes and using `random` as the seed. 
