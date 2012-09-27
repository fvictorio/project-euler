def power_mod(a,b,n):
    if b == 1: return a % 10**n
    
    if b % 2 == 0:
        return (power_mod(a,b/2,n) * power_mod(a,b/2,n)) % 10 ** n
    else:
        return (a* power_mod(a,b/2,n) * power_mod(a,b/2,n)) % 10 ** n
