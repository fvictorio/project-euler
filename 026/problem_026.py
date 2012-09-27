import decimal
from decimal import Decimal

PRECISION = 2000
NUMBERS = 1000

def cycle_size (s):
    for i in xrange(1, len(s)/2):
        if (s[:i]*(len(s)/i+1))[:len(s)] == s: return i
    return 0

decimal.getcontext().prec = PRECISION
decimal.getcontext().rounding = decimal.ROUND_FLOOR

cocients = ['0','1']

for i in xrange(2,NUMBERS):
    cocient = Decimal(1) / Decimal(i)
    cocients.append(str(cocient)[2:])
