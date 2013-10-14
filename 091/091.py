from math import sqrt

def float_equal(a, b):
    return abs(a-b) < 1E-5

def norm2(x, y):
    return sqrt(x*x + y*y)

def right_triangle(x1, y1, x2, y2):
    OP = norm2(x1, y1)
    PQ = norm2(x2-x1, y2-y1)
    QO = norm2(x2, y2)

    a, b, c = sorted([OP, PQ, QO])
    if float_equal(a+b, c): return False #colineales

    return float_equal(a**2 + b**2, c**2)

def calculate(N):
    cant = 0
    for x1 in range(0, N+1):
        for x2 in range(0, N+1):
            for y1 in range(0, N+1):
                for y2 in range(0, N+1):
                    if right_triangle(x1, y1, x2, y2): cant += 1

    return cant
