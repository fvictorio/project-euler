import sys
from itertools import product
from copy import deepcopy
from pprint import pprint
from re import sub

digitos = set([str(i) for i in range(10)])

def row(sudoku, x, y):
    return sudoku[x]

def column(sudoku, x, y):
    return [i[y] for i in sudoku]

def box(sudoku, x, y):
    s_x = 3 * (x/3)
    s_y = 3 * (y/3)
    result = []
    for i in range(s_x, s_x + 3):
        for j in range(s_y, s_y + 3):
            result.append(sudoku[i][j])
    return result

def solve(s):
    sudoku = deepcopy(s)
    while True:
        something_changed = False
        for (i, j) in product(range(9), range(9)):
            if sudoku[i][j] != '0': continue
            candidatos = digitos - set(row(sudoku, i, j) + column(sudoku, i, j) + box(sudoku, i, j))
            if not candidatos:
                sudoku[0][0] = '-'
                return sudoku
            if len(candidatos) == 1:
                sudoku[i][j] = candidatos.pop()
                something_changed = True
                continue
        if not something_changed: break
    for (i, j) in product(range(9), range(9)):
        if sudoku[i][j] != '0': continue
        candidatos = digitos - set(row(sudoku, i, j) + column(sudoku, i, j) + box(sudoku, i, j))
        if not candidatos:
            sudoku[0][0] = '-'
            return sudoku
        for candidato in candidatos:
            sudoku[i][j] = candidato
            intento = solve(sudoku)
            if intento[0][0] != '-': return intento
    return sudoku

sudokus = []
lines_sudoku = open('sudoku.txt').readlines()
for line in lines_sudoku:
    if line[0] == 'G':
        sudokus.append([])
    else:
        sudokus[-1].append(list(sub('[\r\n]', '', line)))

total = 0
i = 0
solved_sudokus = []
for sudoku in sudokus:
    s = solve(sudoku)
    solved_sudokus.append(s)
    if any('0' in i for i in s):
        pprint(s)
    total += int(''.join(s[0][0:3]))
    print i
    i += 1
print total
