def divisors(n):
    i = 2
    result = []
    while (i*i < n):
        if n % i == 0:
            result.append(i)
            result.append(n/i)
        i += 1
    if i*i == n and n % i == 0:
        result.append(i)
    return result

def prod(xs):
    result = 1
    for x in xs:
        result *= x
    return result

def generate_sum_partitions(n, k, minn = -1):
    if minn > n: return []
    if k == 1: return [[n]]
    if minn == -1: minn = 1
    result = []
    for i in range(minn, n):
        for s in generate_sum_partitions(n-i, k-1, i):
            result.append([i] + s)
    return result

def spable(n, k):
    result = []
    for s in generate_sum_partitions(n, k):
        if sum(s) == prod(s): result.append(s)
    return result

def min_sp(k):
    i = 2
    sp = []
    while True:
        sp = spable(i, k)
        if sp: break
        i += 1
    return (i, sp)

def isprime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

#n = 2
#while n < 30:
#    if not isprime(n):
#        i = 2
#        while i < n:
#            print("(%i, %i) => %s" % (n, i, "SI" if spable(n, i) else "NO"))
#            i += 1
#    n += 1
