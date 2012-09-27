def remainder(a, n):
    return ((a-1)**n + (a+1)**n) % a**2

def doble_list(l):
    n = len(l)
    if n % 2 == 1: return False
    return l[:n/2] == l[n/2:]

def r_max(a):
    seen = []
    n = 3
    max_so_far = -1
    while True:
        r = remainder(a, n)
        seen.append(r)
        max_so_far = max(max_so_far, r)
        if doble_list(seen): break
        n += 1
    return max_so_far
