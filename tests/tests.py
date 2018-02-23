import unittest
import numpy as np
from gputils import dyn_mean


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


if __name__ == '__main__':
    unittest.main()
