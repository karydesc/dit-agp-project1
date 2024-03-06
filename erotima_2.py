import itertools
import statistics
import unittest

import utils


class Test(unittest.TestCase):
    def teststats(self):
        expected_total_triangles = 161673
        expected_arithmetic_mean = 3206.82
        expected_median = 2392.50
        expected_std_deviation = 2843.24

        with open("points.txt", 'r') as file:
            lines = file.readlines()

        points = []

        for line in lines:
            x, y = map(int, line.split())
            points.append([x, y])

        combs = itertools.combinations(points, 3)

        validTriangles = []
        for point in combs:
            a, b, c = point
            if utils.isValid(a, b, c):
                validTriangles.append([a, b, c])

        areas = []

        for triangle in validTriangles:
            a, b, c = triangle
            areas.append(utils.TriangleArea(a, b, c))

        self.assertEqual(expected_total_triangles, len(validTriangles), "Total number of triangles doesn't match")
        self.assertAlmostEqual(expected_arithmetic_mean, statistics.mean(areas), places=2,
                               msg="Arithmetic mean doesn't match")
        self.assertAlmostEqual(expected_median, statistics.median(areas), places=2, msg="Median doesn't match")
        self.assertAlmostEqual(expected_std_deviation, statistics.stdev(areas), places=1,
                               msg="Standard deviation doesn't match")
