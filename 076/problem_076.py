class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, p):
        if self.a < p.a: return True
        if self.a > p.a: return False
        return self.b < p.b
    def __eq__(self, p):
        return (not self < p) and (not p < self)

magias = [[0 for j in range(i+1)] for i in range(101)]

def magia(m, n = []):
    if not n: n = m - 1

    #print("calling magia with m=%i and n=%i" % (m, n))

    if n > m: n = m
    if m < 0: return 0
    if m == 0 or m == 1 or n == 1: return 1
    
    if magias[m][n] != 0:
        return magias[m][n]
    else:
        ans = sum(magia(m-i, i) for i in range(1, min(m, n) + 1))
        magias[m][n] = ans
        return ans

