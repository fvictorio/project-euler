from itertools import combinations

def is_prime (n):
    if n == 2: return True
    if (n == 1) or (n % 2 == 0): return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def how_many (s):
    cant = 0
    for i in "123456789":
        n = int(re.sub('\*', i, s))
        if is_prime(n):
            cant += 1
    if s[0] != '*':
        n = int(re.sub('\*', '0', s))
        if is_prime(n):
            cant += 1
    return cant

def calculate (s):
    maxx = 0
    for i in xrange(1,len(s)):
        combs = combinations(range(len(s)), i)
        for comb in combs:
            ss = s
            for c in comb:
                ss = ss[:c] + '*' + ss[c+1:]
            cant = how_many(ss)
            if cant > maxx:
                maxx = cant
    return maxx
