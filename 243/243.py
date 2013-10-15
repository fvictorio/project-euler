from fractions import Fraction as F
from fractions import gcd
from bisect import bisect_left
from math import exp

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

limit = F(15499, 94744)

N       = 1000
NPrimes = 1000000

dp = {}

#primes = [2]
#for n in xrange(3, NPrimes, 2):
#    is_prime = True
#    for p in primes:
#        if p*p > n: break
#        if n%p == 0: 
#            is_prime = False
#            break
#    if is_prime: primes.append(n)

print("listo el pollo")

def isprime(n):
    if binary_search(primes, n) != -1: return True
    for p in primes:
        if p*p > n: break
        if n % p == 0: return False
    return True

def int_log(n, b):
    exp = 0
    while n > 1:
        n /= b
        exp += 1
    return exp

def totient(n):
    if isprime(n):
        return n-1
    if dp.has_key(n):
        return dp[n]
    i = 2
    while i*i <= n:
        if n % i == 0 and gcd(i, n/i) == 1:
            dp[n] = totient(i)*totient(n/i)
            return dp[n]
        i += 1
    # prime power!
    for p in primes:
        if n % p == 0: break
    exp = int_log(n, p)
    return n - p**(exp-1)

def resilience(n):
    return F(totient(n), n-1)

###

# I ended guessing it, starting with 2*3*5*7*11*13*17*19*23*29 and going down
# But the resilience function was useful
