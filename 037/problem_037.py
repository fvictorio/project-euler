def is_prime (n):
    if n == 2: return True
    if (n == 1) or (n % 2 == 0): return False

    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def is_left_truncatable (n):
    sn = str(n)
    for i in xrange(0, len(sn)):
        if not is_prime(int(sn[i:len(sn)])):
            return False
    return True

def is_right_truncatable (n):
    sn = str(n)
    for i in xrange(0, len(sn)):
        if not is_prime(int(sn[0:len(sn)-i])):
            return False
    return True

def is_truncatable (n):
    return is_left_truncatable(n) and is_right_truncatable(n)

if 0:
    for NOW in xrange(6,11):
        for l in left[NOW-1]: 
            for i in xrange(1,10):
                n = int(str(i) + str(l))
                if is_left_truncatable(n):
                    left[NOW].append(n)

        for r in right[NOW-1]:
            for i in xrange(1,10,2):
                n = int(str(r) + str(i))
                if is_right_truncatable(n):
                    right[NOW].append(n)
