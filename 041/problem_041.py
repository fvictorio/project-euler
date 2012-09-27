from itertools import permutations

def is_prime (n):
    if n == 2: return True
    if (n == 1) or (n % 2 == 0): return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

digits = "123456789"

maxx = 0

for i in xrange(1,10):
    perms = permutations(digits[0:i])
    for perm in perms:
        n = int(''.join(perm))
        if is_prime(n) and n > maxx: maxx = n
