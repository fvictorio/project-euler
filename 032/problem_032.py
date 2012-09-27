from itertools import permutations

def is_pandigital(a,b):
    conc = str(a) + str(b) + str(a*b)
    return "123456789" == ''.join(sorted(conc))

def tiene_repetidos(s):
    for i in s:
        if s.count(i) > 1:
            return True
    return False

digits = '123456789'
seen = []
total = 0

if 1:
    for m_size in xrange(1,9):
        m_perms = permutations(digits,m_size)
        for m_perm in m_perms:
            m = int(''.join(m_perm))
            for n in xrange(1,m):
                prod = m*n
                if len(str(m)) + len(str(n)) + len(str(prod)) > 9: 
                    break
                if (set(str(m)) & set(str(n))) != set([]):
                    continue
                if is_pandigital(m,n):
                    print "%i * %i = %i" % (m,n,prod)
                    seen.append(prod)
                    total += prod
