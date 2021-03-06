import unittest, time
import numpy as np
import pandas as pd
from gputils import dyn_mean, dyn_stdev, cosine_similarity


class TestMethods(unittest.TestCase):

    def test_dyn_mean(self):
        # Special cases
        with self.assertRaises(ValueError):
            dyn_mean(69,0,0)
        self.assertEqual(np.mean(np.array(12)),dyn_mean(12, 0, 1))

        # Normal cases
        for i in range(10):
            size = np.random.randint(100, 1001)
            values = np.random.rand(size) * 100
            prev_mean = np.mean(values[:-1])
            curr_mean = np.mean(values)
            test_mean = dyn_mean(values[-1], prev_mean, len(values))
            self.assertAlmostEqual(curr_mean, test_mean, 10)

    def test_dyn_stdev(self):
        # Special cases
        with self.assertRaises(ValueError):
            dyn_stdev(69, 0, 0, 0)
        self.assertEqual(np.std(np.array(12)),dyn_stdev(12, 0, 0, 1))

        # Normal cases
        for i in range(10):
            size = np.random.randint(10000, 100000)
            values = np.random.rand(size) * 100
            prev_mean = np.mean(values[:-1])
            prev_std = np.std(values[:-1])
            t0_trusted = time.time()
            curr_std = np.std(values)
            t1_trusted = time.time()
            t0_test = time.time()
            test_stdev = dyn_stdev(values[-1], prev_std, prev_mean, len(values))
            t1_test = time.time()
            self.assertAlmostEqual(curr_std, test_stdev, 10)
            self.assertLessEqual(t1_test - t0_test, t1_trusted - t0_trusted) # ensuring we are faster

    def test_cosine_similarity(self):
        u = pd.Series([1, 2, 3])
        v = pd.Series([3, 2, 1])
        similarity = cosine_similarity(u, v)
        manual = 10 / (np.sqrt(np.sum(u * u)) * np.sqrt(np.sum(v * v)))
        self.assertEqual(manual, similarity)

        np.random.seed(69)
        E = pd.DataFrame(np.random.randn(4, 3), index=['house', 'rocket', 'science', 'Trump'])
        word = 'science'
        w = E.loc[word]
        similarity = cosine_similarity(E, w)
        self.assertAlmostEqual(1.0, similarity['science'], 10)
        u = E.loc['science']
        v = E.loc['Trump']
        manual = np.sum(u * v) / ((np.sqrt(np.sum(u * u)) * np.sqrt(np.sum(v * v))))
        self.assertAlmostEqual(manual, similarity['Trump'], 5)

if __name__ == '__main__':
    unittest.main()
