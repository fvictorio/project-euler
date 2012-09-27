EPSILON = 10**-5

def expresable (comp, prime):
    n = sqrt((comp-prime)/2)
    return abs(n-int(n)) < EPSILON

def is_prime (n):
    if (n == 1) or (n % 2 == 0): return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True
