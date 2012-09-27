import decimal
from decimal import Decimal

def is_magic_fraction (a, b):
    if (a % 10 == 0) and (b % 10 == 0): return False

    aa = str(a)
    bb = str(b)
    if sorted(aa) == sorted(bb): return False
    
    for i in aa:
        if i in bb:
            aa = list(aa)
            aa.remove(i)
            aa = ''.join(aa)
            bb = list(bb)
            bb.remove(i)
            bb = ''.join(bb)

    aa = int(aa)
    bb = int(bb)

    if bb == 0: return False
    if (aa == a) and (bb == b): return False

    return (Decimal(a)/Decimal(b)) == (Decimal(aa)/Decimal(bb))
