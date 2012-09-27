def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

primes = [i for i in range(1, 50000) if is_prime(i)]

def rad(n):
    if is_prime(n):
        return n
    else:
        result = 1
        for prime in primes:
            if 2*prime > n: break
            if n % prime == 0:
                result *= prime
        return result
