from math import sqrt
from fractions import gcd

def coprimes(a, b):
    return (gcd(a,b) == 1) and (((b-a) % 2) == 1)

def particiones(x, m):
    """
    How many ways to express x = x1 + x2,
    with x1 <= x2 <= m
    """
    
    if x > m:
        a = x - m
        b = x / 2
        if b - a + 1 >= 0:
            return b - a + 1
        else:
            return 0
    else:
        return x/2

def magialoca(M):
    m = 2
    n = 1

    cant = 0

    while True:
        k = 1
        while True:
            a = k*2*m*n
            b = k*(m**2 - n**2)

            if a > M and b > M:
                break
            if a <= M:
                cant += particiones(b, min(a, M))
            if b <= M:
                cant += particiones(a, min(b, M))
            k += 1

        n += 1
        while True:
            if n == m:
                if (m**2 - (m-1)**2) > M: return cant
                n = 1
                m += 1
            if coprimes(m, n): break
            n += 1

    return cant
