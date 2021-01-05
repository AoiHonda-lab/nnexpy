# DataInstance

## Class Variables

`classNumber` (`int`): The number of classes in the `DataInstance`

`nPoints` (`int`): The number of points in the `DataInstance`

`points` (`[DataPoint]`): The points of the `DataInstance`

`dimension` (`int`): The dimension of the `DataInstance`. Corresponds to the `dimension` of the `DataPoint` in `points`

##Constructors

`__init__({'classNumber': classNumber, 'nPoints': nPoints, 'points': points, 'dimension': dimension, 'orientation': orientation})` 

## Methods

`plot(noBack=False, nPoints=self.nPoints)`: Plot `nPoints`randomly selected of the `DataInstance`. If `noBack`, the points with class `0` are ignord

`numpyify()` (`return numpy.array([numpy.array, numpy.array])`): Returns numpy arrays of the points and labels split

`predict(model)` (`return DataInstance`): Returns the `DataInstance` predicted by the Keras + Tensorflow network when feeding the instance `points`

`predictAndEvaluate(model)` (`return float`): Computes the accuracy of the Keras + Tensorflow network over the `DataInstance`

`computeBottleNeckDistance(DataInstance, min_persistence=0, nPoints=self.nPoints, targetCluster=[1])` (`return float`): Computes the bottleneckDistance of the `DataInstance` to another one passed in argument using up to `nPoints` from the instances and restricting the study to points with classes in `targetCluster`  

`newBettiNumbers(targetCluster=[1], threshold=0.05,nPoints=self.nPoints, errorRate=0.005, plot=False)` (`return [int]`): Computes the betti numbers of the `DataInstance` using a custom algorithm for up to `nPoints` evenly distributed in `targetCluster`

