d = {}

def sum_of_divisors(n):
    result = 1
    i = 2
    while i*i < n:
        if n % i == 0:
            result += (i + n/i)
        i += 1
    return result

total = 0
for i in xrange(2,10000):
    i_sum = sum_of_divisors(i)
    d[i] = i_sum
