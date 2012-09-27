factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def chain(n):
    result = 0
    while n > 0:
        result += factorial[n%10]
        n /= 10
    return result


def chain_length(n):
    seen = set([])
    while n not in seen:
        seen.add(n)
        n = chain(n)
    return len(seen)

i = 1
cant = 0
while i < 10**6:
    if chain_length(i) == 60:
        cant += 1
    if i % 10**4 == 0: print i
    i += 1
print cant
