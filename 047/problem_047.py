from itertools import count
def is_prime (n):
    if (n == 2): return True
    if (n == 1) or (n % 2 == 0): return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def factors (n):
    total = 0
    i = 2
    while n > 1:
        if n % i == 0:
            total += 1
            n /= i
            while  n % i == 0:
                n /= i
        i += 1
    return total

if 1:
    n1 = 10
    n2 = 11
    n3 = 12
    n4 = 13

    for i in count(14):
        if (not i % 1000): print i
        n1,n2,n3,n4 = n2,n3,n4,i
        distincts = lambda x: factors(x) == 4
        if all(distincts(j) for j in [n1,n2,n3,n4]):
            print "%i %i %i %i" % (n1,n2,n3,n4)
            break
