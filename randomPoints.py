import utils
import random
import itertools
import statistics

points = []

for i in range(0, 100):  # create list of 100 random points
    points.append([random.randint(-100, 100),
                   random.randint(-100, 100)])  # append points in the form of lists into a list container
combinations = itertools.combinations(points, 3)

validTriangles = []
for point in combinations:  # if a combination is valid append it to "validTriangles" list
    a, b, c = point
    if utils.isValid(a, b, c):
        validTriangles.append([a, b, c])

areas = []

for triangle in validTriangles:  # for every triangle, compute its area.
    a, b, c = triangle
    areas.append(utils.TriangleArea(a, b, c))

print(str(len(validTriangles)) + "  Number of valid Triangles")  # print result
print((str(statistics.mean(areas))) + "  Mean")
print(str(statistics.median(areas)) + " Median")
print(str(statistics.stdev(areas)) + " Standard Deviation")
