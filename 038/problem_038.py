from itertools import permutations

def is_pandigital (n):
    return ''.join(sorted(n)) == "123456789"

def get_product (n):
    result = ''
    i = 1
    while True:
        result += str(n*i)
        if (len(result) == 9) and (is_pandigital(result)): return int(result)
        elif len(result) > 9: return -1
        else: i += 1

digits = "123456789"
maxx = 0

if 1:
    for i in xrange(1,8):
        perms = permutations(digits, i)
        for perm in perms:
            n = int(''.join(perm))
            product = get_product(n)
            if (product != -1) and (product > maxx):
                print "%i forms the product %i" % (n, product)
                maxx = product
