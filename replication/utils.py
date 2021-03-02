def cantor(n):
    res = []
    for i in range(n+1):
        for j in range(n+1):
            res.append([i, j])
    res.sort(key=lambda x: x[0] + x[1])
    return res[1:]


def select_random_cumulative(L):
    import random as r
    item = r.randint(1, sum(L))
    index = -1
    cumul = 0
    while cumul < item:
        index += 1
        cumul += L[index]
    return index
