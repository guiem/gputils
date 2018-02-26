import math

def dyn_mean(val, prev_mean, n):
    """Dynamic mean: computes the mean based on a previous mean plus a new value. Useful when mean is built
    incrementally, it saves the usage of huge arrays.

    Keyword arguments:
    val -- new val to add to the mean
    prev_mean -- previous mean value
    n -- number of total elements in the mean including the new val
    """
    if n < 1:
        raise ValueError("n < 1, mean only defined for a positive number of elements")
    if n == 1:
        return val
    return (prev_mean*(n-1)+val) / n


def dyn_stdev(val, prev_stdev, prev_mean, n):
    """Dynamic stdev: computes the standard deviation based on a previous stdev plus a new value. Useful when stdev
     is built incrementally, it saves the usage of huge arrays.

    Keyword arguments:
    val -- new val to add to the mean
    prev_stdev -- previous stdev value
    n -- number of total elements in the mean including the new val
    """
    if n < 1:
        raise ValueError("n < 1, stdev only defined for a positive number of elements")
    if n == 1:
        return 0
    curr_mean = dyn_mean(val, prev_mean, n)
    return math.sqrt(((n-1)*prev_stdev*prev_stdev + (val - prev_mean)*(val - curr_mean)) / float(n))