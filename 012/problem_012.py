import time
from math import sqrt, ceil

divisors = {1:1}

def count(n):
    if divisors.has_key(n):
        return divisors[n]
    result = 0
    for i in xrange(1,int(sqrt(n) + 1)):
        if n % i == 0:
            result += 2
            if n/i == i:
                result -= 1
    divisors[n] = result
    return result


begin = time.time()
i = 1
while True:
    if i%2 == 0: 
        cant = count(i/2)*count(i+1)
    else:
        cant = count(i)*count((i+1)/2)
    if cant > 500:
        print (i*(i+1))/2
        break
    i += 1
end = time.time()
print end - begin
