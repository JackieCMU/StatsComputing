from KernelSmoother import *
from Kernel import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_smoother_factory(self):

        xs1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        ys1 = [[3], [5], [7]]

        xs2 = [[1], [2], [3]]
        ys2 = [[0], [4], [2]]

        # test Boxcar Kernel in multiple dimensions
        factory1 = smoother_factory(xs1, ys1, BoxcarKernel)
        self.assertEqual(factory1(4)([1,1,1]), 5.0)
        self.assertEqual(factory1(4)([0,0,0]), 4.0)
        self.assertEqual(factory1(0.1)([1,1,1]), 3.0)
        with self.assertRaises(ValueError):
            factory1(-2)([0, 0, 0])

        # test Boxcar Kernel in two dimensions
        factory2 = smoother_factory(xs2, ys2, BoxcarKernel)
        self.assertEqual(factory2(1)([[2]]), 2.0)
        with self.assertRaises(ValueError):
            factory2(1)([[10]])

    def test_make_kernel_smoother(self):

        xs1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        ys1 = [[3], [5], [7]]

        xs2 = [[1], [2], [3]]
        ys2 = [[0], [4], [2]]
        bandwidth = 4

        factory1 = make_kernel_smoother(xs1, ys1, bandwidth, GaussianKernel)
        self.assertEqual(round(factory1([1,1,1]),2), 4.76)

        factory2 = make_kernel_smoother(xs1, ys1, bandwidth, BoxcarKernel)
        self.assertEqual(factory2([1,1,1]), 5.0)

        factory3 = make_kernel_smoother(xs2, ys2, bandwidth, BoxcarKernel)
        with self.assertRaises(ValueError):
            factory3([50])

    def test_EqualResult(self):

        xs1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        ys1 = [[3], [5], [7]]
        bandwidth = 3

        factory1 = make_kernel_smoother(xs1, ys1, bandwidth, GaussianKernel)
        factory2 = smoother_factory(xs1, ys1, GaussianKernel)
        self.assertEqual(factory1([1,1,1]), factory2(bandwidth)([1,1,1]))

if __name__ == '__main__':
    unittest.main()
