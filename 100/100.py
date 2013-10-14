from math import sqrt

def total_discs(blue_discs):
    det = 1.0 + 8.0 * (blue_discs**2.0 - blue_discs)
    return (1.0 + sqrt(det)) / 2.0

def blue_discs(total_discs):
    det = 4.0 + 8.0 * (total_discs**2 - total_discs)
    return (2.0 + sqrt(det)) / 4.0

def integer(n):
    return abs(n - int(n)) < 1E-8

def test(N, Nb):
    return 2*Nb*(Nb-1) - N*(N-1)

def solution(N, Nb):
    return test(N, Nb) == 0

N = 1000000000000
Nb = int(blue_discs(N))
while True:
    while test(N, Nb) < 0:
        Nb += 1
    if solution(N, Nb): break
    while test(N, Nb) > 0:
        Nb -= 1
    if solution(N, Nb): break
    while test(N, Nb) < 0:
        Nb += 1
    if solution(N, Nb): break
    N += 1
    Nb = int(blue_discs(N))
