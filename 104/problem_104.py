def is_pandigital(sn):
    ln = list(str(sn))
    digits = [str(i) for i in range(1, 10)]
    return digits == sorted(ln)

def test_first(n):
    sn = str(n)
    return is_pandigital(sn[:9])

def test_last(n):
    sn = str(n)
    return is_pandigital(sn[-9:])

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n/2)
    else:          return mul(A, pow(mul(A, A), (n-1)/2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]


