from math import sqrt

EPSILON = 10**-5

def is_pentagonal(p):
    n = (1 + sqrt(1 + 24 * p)) / 6
    if (n > 0) and (abs(n - int(n)) < EPSILON):
        return True
    n = (1 - sqrt(1 + 24 * p)) / 6
    if (n > 0) and (abs(n - int(n)) < EPSILON):
        return True
    return False
