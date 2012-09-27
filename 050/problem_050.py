#primes = [2]
#for i in xrange(3,10**6,2):
#    if is_prime(i): primes.append(i)

maxx = 0
cantmax = 0
for i in xrange(len(primes)):
    suma = primes[i]
    for j in count(i+1):
        if j >= len(primes): break
        suma += primes[j]
        if suma > 10**6: break
        cant = j - i + 1
        if (cant > cantmax) and (suma in primes):
            cantmax = cant
            print "between %i and %i" % (i, j)
