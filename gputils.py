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