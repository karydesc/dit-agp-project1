import utils
import random
import itertools
import statistics

points = []
# for i in range(0, 100):
#    points.append([random.randint(-100, 100), random.randint(-100, 100)])
#
# with open("points.txt",'r') as file:
#     pointsList = file.readlines()
#
# for line in pointsList:
#     # Split the line into x and y coordinates
#     x, y = map(int, line.split())
#     # Append the coordinates as a list to the points list
#     points.append([x, y])

combinations = itertools.combinations(points,3)

validTriangles = []
for point in combinations:
    a, b, c = point
    if utils.isValid(a,b,c):
        validTriangles.append([a,b,c])

areas = []

for triangle in validTriangles:
    a, b ,c = triangle
    areas.append(utils.TriangleArea(a,b,c))

print(len(validTriangles))

import unittest

class Test(unittest.TestCase):

    def teststats(self):
        expected_total_triangles = 161671
        expected_arithmetic_mean = 3206.86
        expected_median = 2392.50
        expected_std_deviation = 2843.23

        with open("points.txt", 'r') as file:
            lines = file.readlines()

        points = []

        for line in lines:
            x, y = map(int, line.split())
            points.append([x, y])

        combs = itertools.combinations(points,3)

        validTriangles = []
        for point in combs:
            a, b, c = point
            if utils.isValid(a, b, c):
                validTriangles.append([a, b, c])

        areas = []

        for triangle in validTriangles:
            a, b, c = triangle
            areas.append(utils.TriangleArea(a, b, c))

        print(len(validTriangles))
        self.assertEqual(len(validTriangles), expected_total_triangles, "Total number of triangles doesn't match")
        self.assertAlmostEqual(statistics.mean(areas), expected_arithmetic_mean, places=2, msg="Arithmetic mean doesn't match")
        self.assertAlmostEqual(statistics.median(areas), expected_median, places=2, msg="Median doesn't match")
        self.assertAlmostEqual(statistics.stdev(areas), expected_std_deviation, places=2, msg="Standard deviation doesn't match")


