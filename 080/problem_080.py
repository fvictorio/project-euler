from decimal import getcontext, Decimal

getcontext().prec = 102
exponent = Decimal('0.5')

total = 0
numbers = range(1,101)
for i in range(1, 11):
    numbers.remove(i**2)
for i in numbers:
    a = Decimal(i)**exponent
    sa = str(a)
    point = sa.index('.')
    suma = sum(int(i) for i in sa[0:point] + sa[point+1:-2])
    total += suma
print total
