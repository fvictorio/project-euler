from fractions import gcd

def odd(n):
    return n%2 == 1

TOP = 1500000
perimeters = {}

m = 2
while True:
    n = 1
    if (2*m**2 + 2*m*n) > TOP: break
    while True:
        if (2*m**2 + 2*m*n) > TOP: break
        if gcd(m, n) != 1 or (odd(m) and odd(n)):
            n += 1
            if m == n: break
            continue

        i = 1
        while True:
            a = i * (m**2 - n**2)
            b = i * (2*m*n)
            c = i * (m**2 + n**2)
            lados = [a, b, c]
            lados.sort()
            p = sum(lados)
            if p > TOP: break
            if perimeters.has_key(p):
                if not lados in perimeters[p]:
                    perimeters[p].append(lados)
            else:
                perimeters[p] = [lados]
            i += 1
        n += 1
        if m == n: break
    m += 1

print sum(1 for i in perimeters if len(perimeters[i]) == 1)
