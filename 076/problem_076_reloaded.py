# Using Euler transform
# http://mathworld.wolfram.com/EulerTransform.html

def a(n):
    return 1

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

print(b(100) - 1)
# The '- 1' is because the transform counts
# the number itself.
