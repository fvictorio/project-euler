import decimal
from decimal import Decimal

decimal.getcontext().prec = 800
decimal.getcontext().rounding = decimal.ROUND_FLOOR

def magia(n):
    n = Decimal(n).sqrt()
    answer = []
    seen = set([])
    while True:
        r = int(n) # integer
        f = (n - r) # Decimal
        #print f
        answer.append(r)
        if str(f)[:10] in seen:
            break
        seen.add(str(f)[:10])
        n = 1/f
    return answer
