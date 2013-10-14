from math import sqrt
from fractions import gcd

def coprimes(a, b, c):
    gab = gcd(a,b)
    gbc = gcd(b,c)
    return gab != gbc or gab == 1

def inc(a, maxx):
    i = 1
    a[i] += 1
    while a[i] > maxx:
        if i+1 == len(a): return False
        i += 1
        a[i] += 1
        j = i
        while j > 1:
            j -= 1
            a[j] = a[j+1]
    return True

def perfect_square(x):
    sx = round(sqrt(x))
    pa = (sx-1)**2 == x
    pb = sx**2 == x
    pc = (sx+1)**2 == x
    return pa or pb or pc

def integer(x):
    return abs(x-round(x)) < 1E-5

def integer_route(cub):
    A = cub[0]
    B = cub[1]
    C = cub[2]

    det = A**2 + (B+C)**2
    if not perfect_square(det): return False

    a = A*C / (B+C)
    #b = B*A / (A+C)
    #c = C*B / (A+B)

    d1 = sqrt(det)
    #d2 = sqrt(b**2 + A**2) + sqrt((B-b)**2 + C**2)
    #d3 = sqrt(c**2 + B**2) + sqrt((C-c)**2 + A**2)

    #return integer(min(d1, d2, d3))
    return integer(d1)

def red(c):
    g = gcd(c[0], c[1])
    return (c[0]/g, c[1]/g, c[2]/g)

dp = {}
M = 1
cuboid = [1.0, 1.0, 1.0]
cant = 0
while True:
    if not coprimes(cuboid[0], cuboid[1], cuboid[2]):
        if red(cuboid) in dp:
            cant += 1
    elif integer_route(cuboid):
        #print(cuboid)
        dp[(cuboid[0], cuboid[1], cuboid[2])] = 1
        cant += 1
    if not inc(cuboid, M):
        print("M: %i\n cant: %i\n-----" % (M, cant))
        M += 1
        if M > 500: break
        cuboid = [1.0*M, 1.0, 1.0]

print(M)
print(cant)
