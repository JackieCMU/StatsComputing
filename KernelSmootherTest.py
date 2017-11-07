from KernelSmoother import *
from Kernel import *
import unittest

class TestStringMethods(unittest.TestCase):

    xs1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    ys1 = [[3], [5], [7]]

    xs2 = [[1], [2], [3]]
    ys2 = [[0], [4], [2]]

    def smoother_factory_test(self):

        # test Boxcar Kernel in multiple dimensions
        factory1 = smoother_factory(xs1, ys1, BoxcarKernel)
        self.assertTrue(factory1(-2)([0, 0, 0]) == "The bandwidth cannot be negative")

        self.assertTrue(factory1(4)([1,1,1]) == 5.0)
        self.assertTrue(factory1(4)([0,0,0]) == 4.0)
        self.assertTrue(factory1(0.1)([1,1,1]) == 3.0)

        # test Boxcar Kernel in two dimensions
        factory2 = smoother_factory(xs2, ys2, BoxcarKernel)
        self.assertTrue(factory2(1)([[10]]) == "The data is not enough to make an estimation"
)
        self.assertTrue(factory2(1)([[2]]) == 2.0)

    def make_kernel_smoother(self):
        bandwidth = 4
        factory1 = make_kernel_smoother(xs1, ys1, bandwidth, GaussianKernel)
        self.assertTrue(round(factory1([1,1,1]),2) == 4.76)

        factory2 = make_kernel_smoother(xs1, ys1, bandwidth, BoxcarKernel)
        self.assertTrue(factory2([1,1,1]) == 5.0)

        factory3 = make_kernel_smoother(xs2, ys2, bandwidth, BoxcarKernel)
        self.assertTrue(factory3([50]) == "The data is not enough to make an estimation")

    def EqualResult(self):
        bandwidth = 3
        factory1 = make_kernel_smoother(xs1, ys1, bandwidth, GaussianKernel)
        factory2 = smoother_factory(xs1, ys1, GaussianKernel)
        self.assertTrue(factory1([1,1,1]) == factory2(bandwidth)([1,1,1]))

if __name__ == '__main__':
    print(unittest.main())