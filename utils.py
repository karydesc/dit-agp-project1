import math
import random
import statistics


def distance(vec1, vec2):
    return math.sqrt((vec1[0] - vec2[0]) ** 2 + (vec1[1] - vec2[1]) ** 2)


def TriangleArea(pA, pB, pC):
    a = distance(pB, pC)
    b = distance(pA, pC)
    c = distance(pA, pB)
    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def mean(a):
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)


def median(a):
    a.sort()
    return a[len(a) // 2]


def dev(n):
    _mean = sum(n) / len(n)
    SUM = 0
    for i in n:
        SUM += (i - mean) ** 2

    stdeV = math.sqrt(SUM / (len(n) - 1))
    return stdeV


def isValid(p1, p2, p3):
    side1 = distance(p1, p2)
    side2 = distance(p2, p3)
    side3 = distance(p1, p3)
    s = (side1 + side2 + side3) / 2
    return s * (s - side1) * (s - side2) * (s - side3) > 0


def L_range(a):
    a.sort()
    return [a[0], a[len(a) - 1]]
