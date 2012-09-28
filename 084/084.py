from random import choice, shuffle
from heapq import nlargest

def roll_dices(no_sides):
    return choice(range(no_sides)) + 1

def next_railway(squares, current):
    no_squares = len(squares)
    i = (current + 1) % no_squares
    while True:
        if squares[i] in ['R1', 'R2', 'R3', 'R4']:
            return i
        i = (i + 1) % no_squares


def next_utility(squares, current):
    no_squares = len(squares)
    i = (current + 1) % no_squares
    while True:
        if squares[i] in ['U1', 'U2']:
            return i
        i = (i + 1) % no_squares

squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

community_chest_cards = [1, 2] + [0]*14
chance_cards = range(1,11) + [0]*6

shuffle(community_chest_cards)
shuffle(chance_cards)

go_square = squares.index('GO')
jail_square = squares.index('JAIL')
go_to_jail_square = squares.index('G2J')
c1_square = squares.index('C1')
e3_square = squares.index('E3')
h2_square = squares.index('H2')
r1_square = squares.index('R1')

cc_squares = [squares.index(i) for i in ['CC1', 'CC2', 'CC3']]
ch_squares = [squares.index(i) for i in ['CH1', 'CH2', 'CH3']]

N = 1000000
no_sides = 4
no_squares = len(squares)
no_consecutive_doubles = 0

visits = [0 for i in range(no_squares)]

current_square = 0
for i in range(1, N+1):
    if i % (N/100) == 0:
        pass
        #print(i / (N/100))

    visits[current_square] += 1

    dice1 = roll_dices(no_sides)
    dice2 = roll_dices(no_sides)
    
    if dice1 == dice2:
        no_consecutive_doubles += 1
    else:
        no_consecutive_doubles = 0

    if no_consecutive_doubles == 3:
        no_consecutive_doubles = 0
        current_square = jail_square
        continue

    advance = dice1 + dice2
    current_square = (current_square + advance) % no_squares

    j = 0
    while j < 1:
        j += 1
        if current_square == go_to_jail_square:
            current_square = jail_square
        elif current_square in cc_squares:
            cc_card = community_chest_cards[0]
            if cc_card == 1:
                current_square = go_square
            elif cc_card == 2:
                current_square = jail_square
            community_chest_cards = community_chest_cards[1:] + [cc_card]
        elif current_square in ch_squares:
            ch_card = chance_cards[0]
            if ch_card == 1:
                current_square = go_square
            elif ch_card == 2:
                current_square = jail_square
            elif ch_card == 3:
                current_square = c1_square
            elif ch_card == 4:
                current_square = e3_square
            elif ch_card == 5:
                current_square = h2_square
            elif ch_card == 6:
                current_square = r1_square
            elif ch_card in [7, 8]:
                current_square = next_railway(squares, current_square)
            elif ch_card == 9:
                current_square = next_utility(squares, current_square)
            elif ch_card == 10:
                current_square = (current_square + no_squares - 3) % no_squares
                j -= 1
            chance_cards = chance_cards[1:] + [ch_card]

enum_visits = [(i[1], i[0]) for i in enumerate(visits)]
top_three = nlargest(3, enum_visits)
print(top_three)
