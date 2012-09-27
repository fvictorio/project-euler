from itertools import permutations

def check(a, b, c, d, e, f, g, h, i, j):
    n = a + b + c
    return (d + c + e == n) and (f + e + g == n) and (h + g + i == n) and (j + i + b == n)

for a in range(6,0,-1):
    for (d, f, h, j) in permutations(range(9, a, -1) + [10], 4):
        numbers = range(1, 11)
        numbers.remove(a)
        numbers.remove(d)
        numbers.remove(f)
        numbers.remove(h)
        numbers.remove(j)
        for (b, c, e, g, i) in permutations(numbers):
            if check(a, b, c, d, e, f, g, h, i, j):
                print (a, b, c, d, e, f, g, h, i, j)
