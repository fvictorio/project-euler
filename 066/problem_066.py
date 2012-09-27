from math import sqrt, floor
from fractions import Fraction as F

def continued_fraction(s):
    """
    Returns the list a = [a0, a1, ...] used
    to approximate sqrt(s) through continued
    fractions.
    """
    m = [0]
    d = [1]
    a = [int(floor(sqrt(s)))]
    seen = set([])
    while True:
        if (m[-1], d[-1], a[-1]) in seen: break
        seen.add( (m[-1], d[-1], a[-1]) )
        
        m.append(d[-1]*a[-1] - m[-1])
        d.append((s - m[-1]**2)/d[-1])
        a.append(int(floor((a[0] + m[-1])/d[-1])))
    return a[:-1]

def evaluate_continued_fraction(a):
    assert len(a) >= 2
    
    result = F(1, a[-1])
    for i in reversed(a[1:-1]):
        result = i + result
        result = result**-1
    result = a[0] + result

    return result

def evaluate_diophantine(x, y, D):
    return x**2 - D*y**2 == 1

def solve_diophantine(D):
    cf = continued_fraction(D)
    a = [cf[0]]
    cf = cf[1:]
    i = 0
    while True:
        a.append(cf[i])
        approximation = evaluate_continued_fraction(a)
        x, y = approximation.numerator, approximation.denominator
        if evaluate_diophantine(x, y, D):
            return (x, y)
        i += 1
        if i == len(cf):
            i = 0

def is_square(n):
    sqn = round(n**0.5)
    return (sqn**2 == n) or ((sqn-1)**2 == n) or ((sqn+1)**2 == n)

max_so_far = 0
max_i = 0
for i in range(1, 1001):
    if is_square(i): continue

    x, y = solve_diophantine(i)
    if x > max_so_far:
        max_so_far, max_i = x, i
print max_i
