# Using Euler transform
# http://mathworld.wolfram.com/EulerTransform.html

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def a(n):
    if is_prime(n):
        return 1
    return 0

def c(n):
    result = 0
    for d in range(1, n+1):
        if n % d == 0:
            result += d*a(d)
    return result

b_d = {} # for dynamism

def b(n):
    if n == 1: return c(1)
    if b_d.has_key(n):
        return b_d[n]
    s = sum(c(k) * b(n-k) for k in range(1, n))
    r = (c(n) + s) / n
    b_d[n] = r
    return r

i = 10
while True:
    if b(i) > 5000: break
    i += 1

print i
