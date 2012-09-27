def is_abundant (n):
    divisors = [1]
    i = 2
    while i*i < n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
        i += 1
    if i*i == n:
        divisors.append(i)
    return sum(divisors) > n
