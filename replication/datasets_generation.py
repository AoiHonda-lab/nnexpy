def create_data_descriptor(*args, **kwargs):
    import nnexpy_min
    import random as r
    from utils import select_random_cumulative
    threshold = kwargs.get('threshold', 0.05)
    minStrataThickness = kwargs.get('minStrataThickness', threshold * 0.9)
    strataDensity = kwargs.get('strataDensity', 0.2)
    dimension = kwargs.get('dimension', 2)
    dimensionDistribution = kwargs.get('dimensionDistribution', None)
    maxUnsuccessfulAttempts = kwargs.get('maxUnsuccessfulAttempts', 1000)
    seed = kwargs.get('seed', None)
    if seed:
        r.seed(seed)
    if dimensionDistribution == None:
        dimensionDistribution = [0] * dimension
        dimensionDistribution[-1] = 1
    centerList = []
    radiusList = []
    attempts = 0
    while sum(dimensionDistribution) > 0 and attempts < maxUnsuccessfulAttempts:
        candidate = nnexpy_min.DataPoint()
        if len(centerList) == 0:
            minDistPoints = threshold * (sum(dimensionDistribution) + 2)
        else:
            minDistPoints = min([candidate.distanceTo(centerList[i]) -
                                 radiusList[i][-1][1] for i in range(len(centerList))])
        distBounds = []
        for coord in candidate.coordinates:
            distBounds.append(coord)
            distBounds.append(1-coord)
        minDistBounds = min(distBounds) + threshold
        minDist = min(minDistPoints, minDistBounds)
        if minDist > 2*threshold:
            attempts = 0
            maxStrata = int((minDist - 2*threshold)//threshold)
            dim = select_random_cumulative(dimensionDistribution)
            centerList.append(candidate)
            radius = []
            if dim == 0:
                radius.append((0, r.uniform(minStrataThickness, threshold)))
            else:
                r1 = r.uniform(minStrataThickness, threshold)
                r2 = r.uniform(minStrataThickness, threshold)
                radius.append((min(r1, r2), max(r1, r2)))
            dimensionDistribution[dim] -= 1
            a = r.random()
            while a < strataDensity and sum(dimensionDistribution[1:]) > 0 and maxStrata > 0:
                maxStrata -= 1
                dim = select_random_cumulative(dimensionDistribution[1:])
                r1 = threshold * len(radius) + \
                    r.uniform(minStrataThickness, threshold)
                r2 = threshold * len(radius) + \
                    r.uniform(minStrataThickness, threshold)
                radius.append((min(r1, r2), max(r1, r2)))
                dimensionDistribution[dim + 1] -= 1
                a = r.random()
            radiusList.append(radius)
        attempts += 1
    if attempts >= 1000:
        raise Exception(
            "Unable to generate all the points, try with a smaller threshold")
    return nnexpy_min.DataDescriptor(dimension=dimension, centerList=centerList, radiusList=radiusList, nHoles=len(centerList))


def generate_descriptor(homology, *args, ** kwargs):
    threshold = kwargs.get('initial_threshold', 0.05)
    threshold_decay = kwargs.get('threshold_decay', 0.01)
    seed = kwargs.get('seed', None)
    fail = True
    descriptor = None
    while threshold > 0 and fail:
        try:
            fail = False
            descriptor = create_data_descriptor(
                dimensionDistribution=homology.copy(), threshold=threshold, seed=seed)
        except:
            threshold -= threshold_decay
            fail = True

    return (descriptor, threshold)
