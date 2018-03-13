import math
import pandas as pd
import numpy as np


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


def cosine_similarity(u, v):
    """Cosine similarity: computes the standard cosine similarity between two vectors or a matrix of vectors and a
    vector.
    Returns the cosine similarity between u and v, or list of similarities from every vector in u (if it is a matrix)
    with regards to v.

    Note: for simplicity the vectors should be pd.Series or u could be a pd.DataFrame if matrix product, you can
    add compatibility with other data entries if needed, fork and pull request! :)

    Keyword arguments:
    u -- vector of dimesions 1xn or matrix of dimensions mxn (where m is the number of vectors)
    v -- vector of dimensions 1xn
    """
    dot = u.dot(v.transpose())
    axis = 0 if len(u.shape) < 2 or u.shape[1] < 2 else 1
    norm_u = np.linalg.norm(u, axis=axis)
    norm_v = np.linalg.norm(v)
    similarity = dot / (norm_u * norm_v)
    return similarity