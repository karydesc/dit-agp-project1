import math


def Distance(vec1, vec2):
    return math.sqrt((vec1[0] - vec2[0]) ** 2 + (vec1[1] - vec2[1]) ** 2)


def TriangleArea(pA,pB,pC):
    a = Distance(pB, pC)
    b = Distance(pA, pC)
    c = Distance(pA, pB)
    s = (a+b+c)/2
    factor = int(math.sqrt(s*(s-a)*(s-b)*(s-c)) > 0) # if triangle doesnt exist, the fucntion will return zero
    return math.sqrt(s*(s-a)*(s-b)*(s-c) * factor)


print("Area: " + str(TriangleArea([1,4], [3,0], [1,0])))
