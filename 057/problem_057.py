from fractions import Fraction

f = {0:Fraction(1,2)}

def w_get_fraction(prec):
    if f.has_key(prec):
        return f[prec]
    n = Fraction(1)/Fraction(str(2+w_get_fraction(prec-1)))
    f[prec] = n
    return n

def get_fraction(prec):
    return Fraction(1) + w_get_fraction(prec)

if 1:
    cant = 0
    for i in xrange(1000):
        print i
        n = get_fraction(i)
        if len(str(n.numerator)) > len(str(n.denominator)):
            cant += 1
