import unittest
import numpy as np
from gradient import gradient_descent


class TestGradientDescent(unittest.TestCase):
    def setUp(self):  # Set up test data
        self.a = 4
        self.b = 2
        self.sigma = 0.05
        self.n = 100
        np.random.seed(5)
        self.x = np.linspace(-5, 5, self.n)
        self.y = self.a * self.x + self.b + np.random.normal(
            0, self.sigma, self.n)

    def test_gradient_descent(self):  # test gradient_descent
        gamma = 0.002
        steps = 500
        a_s, b_s, losses = gradient_descent(self.x, self.y, gamma, steps)

        self.assertEqual(len(a_s), steps + 1)
        self.assertEqual(len(b_s), steps + 1)
        self.assertEqual(len(losses), steps)

        self.assertAlmostEqual(a_s[-1], self.a, delta=0.5)
        self.assertAlmostEqual(b_s[-1], self.b, delta=0.5)

        self.assertLess(losses[-1], losses[0])


if __name__ == '__main__':
    unittest.main()
