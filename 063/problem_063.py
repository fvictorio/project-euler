def is_n_power(a, n):
    an = len(str(a**n))
    if an < n: return -1
    elif an == n: return 0
    elif an > n: return 1
