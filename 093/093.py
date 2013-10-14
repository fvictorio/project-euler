from itertools import permutations, combinations

def eval_try(s):
    try:
        return eval(s)
    except ZeroDivisionError:
        return -1

def float_equal(a, b):
    return abs(a-b) < 1E-5

def positive_integer(n):
    rn = round(n)
    if not float_equal(n, rn): return False
    if rn < 1: return False
    return True

def combine(digits):
    result = set([])

    for xs in permutations(digits):
        a = 1.0 * xs[0]
        b = 1.0 * xs[1]
        c = 1.0 * xs[2]
        d = 1.0 * xs[3]
        
        for op1 in ["+", "-", "*", "/"]:
            for op2 in ["+", "-", "*", "/"]:
                for op3 in ["+", "-", "*", "/"]:
                    comb = []

                    comb.append("%f %s %f %s %f %s %f" % (a, op1, b, op2, c, op3, d))

                    comb.append("(%f %s %f) %s %f %s %f" % (a, op1, b, op2, c, op3, d))
                    comb.append("%f %s (%f %s %f) %s %f" % (a, op1, b, op2, c, op3, d))
                    comb.append("%f %s %f %s (%f %s %f)" % (a, op1, b, op2, c, op3, d))
                    comb.append("(%f %s %f) %s (%f %s %f)" % (a, op1, b, op2, c, op3, d))

                    comb.append("(%f %s %f %s %f) %s %f" % (a, op1, b, op2, c, op3, d))
                    comb.append("%f %s (%f %s %f %s %f)" % (a, op1, b, op2, c, op3, d))

                    comb.append("((%f %s %f) %s %f) %s %f" % (a, op1, b, op2, c, op3, d))
                    comb.append("(%f %s (%f %s %f)) %s %f" % (a, op1, b, op2, c, op3, d))
                    comb.append("%f %s (%f %s (%f %s %f))" % (a, op1, b, op2, c, op3, d))
                    comb.append("%f %s ((%f %s %f) %s %f)" % (a, op1, b, op2, c, op3, d))

                    for s in comb:
                        n = eval_try(s)
                        if positive_integer(n):
                            result.add(round(n))

    return result

def longest_sequence(s):
    i = 1
    for elem in list(sorted(s)):
        if elem != i: break
        i += 1
    return i-1

foo = []
for c in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
    foo.append( (c, longest_sequence(combine(c))) )
