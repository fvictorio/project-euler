set89 = set([89])
set1 = set([1])

def sumar(n):
    return sum(int(i)**2 for i in str(n))

def loop(n):
    global set89
    global set1
    seen = set([])
    while True:
        seen.add(n)
        if n in set89:
            set89 = set89.union(seen)
            return
        if n in set1:
            set1 = set1.union(seen)
            return
        n = sumar(n)
