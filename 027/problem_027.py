def generate_formula (a, b):
    return lambda n: n**2 + a*n + b

def is_prime (n):
    if (n == 1) or (n % 2 == 0): return False
    if n == 2: return True

    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def how_many_primes (f):
    i = 0
    while True:
        if not is_prime(abs(f(i))): return i
        i += 1

max_so_far = 40
max_coefficients = (1,41)

for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        f = generate_formula(a, b)
        if not is_prime(f(max_so_far + 1)): continue # ya no va a ser mejor
        primes_generated = how_many_primes(f)
        if primes_generated > max_so_far:
            max_so_far = primes_generated
            max_coefficients = (a, b)
