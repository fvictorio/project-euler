import sys

if 0:
    primes = [3]
    for i in xrange(5,10**7,2):
        for p in primes:
            if (p*p > i) or (i % p == 0): break
        if p*p > i: primes.append(i)

def es_grupo_loco (g):
    combs = combinations(g,2)
    for comb in combs:
        if not (int(str(comb[0]) + str(comb[1]))) in primes: return False
        if not (int(str(comb[1]) + str(comb[0]))) in primes: return False
    return True

sols = []

if 1:
    for ai in xrange(len(primes)):
        a = primes[ai]
        if a > 10**4: break
        print a
        sys.stdout.flush()
        for bi in xrange(ai+1, len(primes)):
            b = primes[bi]
            if b > 10**4: break
            if not es_grupo_loco([a,b]): continue
            for ci in xrange(bi+1, len(primes)):
                c = primes[ci]
                if c > 10**4: break
                if not es_grupo_loco([a,b,c]): continue
                for di in xrange(ci+1, len(primes)):
                    d = primes[di]
                    if d > 10**4: break
                    if not es_grupo_loco([a,b,c,d]): continue
                    for ei in xrange(di+1, len(primes)):
                        e = primes[ei]
                        if e > 10**4: break
                        if es_grupo_loco([a,b,c,d,e]):
                            sols.append([a,b,c,d,e])
