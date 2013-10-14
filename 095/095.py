MAX_N = 1000000

criba = {} # divisors
lac = {} # longest amicable chain

for i in range(2, MAX_N + 1):
    criba[i] = [1]
    lac[i] = 0

i = 2
while 2*i <= MAX_N:
    n = 2*i
    while n <= MAX_N:
        criba[n].append(i)
        n += i
    i += 1

best_lac = 1
min_elem = 28
for i in range(2, MAX_N + 1):
    a = i

    length = 1
    loop = True

    seen = set([a])
    while True:
        na = sum(criba[a])
        if na == i:
            break
        if na in seen:
            loop = False
            break
        if na == 1 or na > MAX_N:
            loop = False
            break
        seen.add(na)
        length += 1
        a = na
    if loop and length > best_lac:
        best_lac = length
        min_elem = min(seen)


#for i in range(2, MAX_N + 1):
#    seen = set([i])
#    loop = True
#    length = 1
#    a = i
#    while True:
#        na = sum(criba[a])
#        if na in seen:
#            break
#        if na == 1 or na > MAX_N:
#            loop = False
#            break
#        seen.add(na)
#        length += 1
#        a = na
#    if loop:
#        for elem in seen:
#            lac[elem] = length
#    else:
#        for elem in seen:
#            lac[elem] = -1
