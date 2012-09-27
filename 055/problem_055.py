def is_palyndromic (n):
    return n == int(''.join(reversed(str(n))))

def is_lychrel (n):
    n += int(''.join(reversed(str(n))))
    cant = 1
    while not is_palyndromic(n) and cant < 50:
        n += int(''.join(reversed(str(n))))
        cant += 1
    return cant == 50
