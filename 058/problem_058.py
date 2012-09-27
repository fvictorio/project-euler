def is_prime (n):
    if n == 2: return True
    if (n == 1) or (n % 2 == 0): return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def how_many (side):
    side2 = side**2
    dec = side - 1
    return sum(map(is_prime, [side2, side2 - dec, side2 - 2*dec, side2 - 3*dec]))
