# Functions taken from http://wiki.python.org/moin/ProblemSets/99 Prolog Problems Solutions
import itertools
from operator import mul

def prime_factors(value):
    if value > 3:
        for this in itertools.chain(iter([2]), xrange(3, int(value ** 0.5)+1, 2)):
            if this*this > value:
                break
            while not (value % this):
                if value == this: break
                value /= this
                yield this
    yield value

def prime_factors_mult(n):
    res = list(prime_factors(n))
    return sorted([fact, res.count(fact)] for fact in set (res))

def totient(n):
    if n == 1: return 1

    return reduce(mul, [(p-1) * p**(m-1) for p,m in prime_factors_mult(n)])
