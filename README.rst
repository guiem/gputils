============================================================
General Python Utils (or Guiem's Python Utils :trollface:)
============================================================

.. image:: https://coveralls.io/repos/github/guiem/gputils/badge.svg?branch=master
    :target: https://coveralls.io/github/guiem/gputils?branch=master

**gputils** is a library that contains a variety of utilities that may come handy in diverse projects.

Installation
------------

:code:`pip install gputils`

Index of utilities
------------------
- :code:`dyn_mean`: computes the mean based on a previous mean plus a new value. Useful when mean is built incrementally, it saves the usage of huge arrays.
- :code:`dyn_stdev`: computes the stdev based on a previous stdev plus a new value.
- :code:`cosine_similarity`: computes the cosine similarity between two vectors or matrix and vector.