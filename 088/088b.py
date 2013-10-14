def prod(xs):
    result = 1
    for x in xs:
        result *= x
    return result

def inc(a, maxx):
    i = 0
    a[i] += 1
    while prod(a) > maxx:
        if i+1 == len(a): return False
        i += 1
        a[i] += 1
        j = i
        while j > 0:
            j -= 1
            a[j] = a[j+1]
    return True

###

MAX_K = 12000

minsp = {}

for k in range(2, MAX_K+1):
    minsp[k] = 2*k

for no_factors in range(2, 15): # 14 = floor(log2(12000))
    factors = [2] * no_factors
    while True:
        n = prod(factors)
        k = no_factors + n - sum(factors)
        if k <= MAX_K:
            minsp[k] = min(minsp[k], n)
        if not inc(factors, 2 * MAX_K): break
