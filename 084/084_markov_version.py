import numpy
from numpy.linalg import matrix_power
from heapq import nlargest


def nr(squares, current):
    no_squares = len(squares)
    i = (current + 1) % no_squares
    while True:
        if squares[i] in ['R1', 'R2', 'R3', 'R4']:
            return i
        i = (i + 1) % no_squares


def nu(squares, current):
    no_squares = len(squares)
    i = (current + 1) % no_squares
    while True:
        if squares[i] in ['U1', 'U2']:
            return i
        i = (i + 1) % no_squares

squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

go_square = squares.index('GO')
jail_square = squares.index('JAIL')
go_to_jail_square = squares.index('G2J')
c1_square = squares.index('C1')
e3_square = squares.index('E3')
h2_square = squares.index('H2')
r1_square = squares.index('R1')

p_advance = {2  : 1.0/16.0,
             3  : 2.0/16.0,
             4  : 3.0/16.0,
             5  : 4.0/16.0,
             6  : 3.0/16.0,
             7  : 2.0/16.0,
             8  : 1.0/16.0}


N = 40
sides = 4

M = [[0 for i in range(N)] for j in range(N)]

for square in range(N):
    for adv in range(2, 2*sides+1):
        if square == 26 and adv == 12:
            pass
        new_square = (square + adv) % N
        if squares[new_square] == 'G2J':
            M[square][jail_square] += p_advance[adv]
        elif squares[new_square] in ['CC1', 'CC2', 'CC3']:
            M[square][new_square]  += p_advance[adv] * 14.0/16.0
            M[square][go_square]   += p_advance[adv] * 1.0/16.0
            M[square][jail_square] += p_advance[adv] * 1.0/16.0
        elif squares[new_square] in ['CH1', 'CH2', 'CH3']:
            M[square][new_square]                 += p_advance[adv] * 6.0/16.0
            M[square][go_square]                  += p_advance[adv] * 1.0/16.0
            M[square][jail_square]                += p_advance[adv] * 1.0/16.0
            M[square][c1_square]                  += p_advance[adv] * 1.0/16.0
            M[square][e3_square]                  += p_advance[adv] * 1.0/16.0
            M[square][h2_square]                  += p_advance[adv] * 1.0/16.0
            M[square][r1_square]                  += p_advance[adv] * 1.0/16.0
            M[square][nr(squares, new_square)]    += p_advance[adv] * 2.0/16.0
            M[square][nu(squares, new_square)]    += p_advance[adv] * 1.0/16.0
            M[square][new_square-3]               += p_advance[adv] * 1.0/16.0
        else:
            M[square][new_square] += p_advance[adv]

MM = numpy.asarray(M)
MM_100 = matrix_power(MM, 100)
total_prob = sum(MM_100/N)
total_prob_enum = [(i[1], i[0]) for i in enumerate(total_prob)]
top_three = nlargest(3, total_prob_enum)
print(top_three)
