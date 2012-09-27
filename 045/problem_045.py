from math import sqrt

EPSILON = 10**-5

def is_triangle (n):
    sol = (1 - sqrt(1 + 8*n))/2
    if (sol > 0) and (abs(sol-int(sol)) < EPSILON): return True
    sol = (1 + sqrt(1 + 8*n))/2
    if (sol > 0) and (abs(sol-int(sol)) < EPSILON): return True
    return False

def is_pentagonal (n):
    sol = (1 + sqrt(1 + 24*n)) / 6
    if (sol > 0) and (abs(sol - int(sol)) < EPSILON): return True
    sol = (1 - sqrt(1 + 24*n)) / 6
    if (sol > 0) and (abs(sol - int(sol)) < EPSILON): return True
    return False

def is_hexagonal (n):
    sol = (1 + sqrt(1 + 8*n))/4
    if (sol > 0) and (abs(sol - int(sol)) < EPSILON): return True
    sol = (1 - sqrt(1 + 8*n))/4
    if (sol > 0) and (abs(sol - int(sol)) < EPSILON): return True
    return False
