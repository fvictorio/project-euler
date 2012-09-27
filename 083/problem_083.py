from copy import deepcopy

#matrix = [[131, 673, 234, 103, 18],
#          [201, 96, 342, 965, 150],
#          [630, 803, 746, 422, 111],
#          [537, 699, 497, 121, 956],
#          [805, 732, 524, 37, 331]]

matrix = open('matrix.txt').readlines()
matrix = [[int(i) for i in re.sub('[\r\n]', '', j).split(',')] for j in matrix]

N = len(matrix)
minimal = [[0 for i in j] for j in matrix]

# primero busco la mejor solucion yendo solo para abajo y a la derecha
minimal[N-1][N-1] = matrix[N-1][N-1]
for i in reversed(range(N-1)):
    minimal[N-1][i] = matrix[N-1][i] + minimal[N-1][i+1]
    minimal[i][N-1] = matrix[i][N-1] + minimal[i+1][N-1]
for i in reversed(range(N-1)):
    minimal[i][i] = matrix[i][i] + min(minimal[i+1][i], minimal[i][i+1])
    for j in reversed(range(i)):
        minimal[j][i] = matrix[j][i] + min(minimal[j][i+1], minimal[j+1][i])
        minimal[i][j] = matrix[i][j] + min(minimal[i+1][j], minimal[i][j+1])

# y ahora lo mejoro agregando la posibilidad de ir para arriba
# y para la izquierda hasta que no pueda mejorarse

while True:
    mejora_izquierda = False
    for i in range(N):
        for j in range(1, N):
            if minimal[i][j] > minimal[i][j-1] + matrix[i][j]:
                mejora_izquierda = True
                minimal[i][j] = minimal[i][j-1] + matrix[i][j]
    mejora_derecha = False
    for i in range(N):
        for j in range(N-1):
            if minimal[i][j] > minimal[i][j+1] + matrix[i][j]:
                mejora_derecha = True
                minimal[i][j] = minimal[i][j+1] + matrix[i][j]
    mejora_arriba = False
    for i in range(1, N):
        for j in range(N):
            if minimal[i][j] > minimal[i-1][j] + matrix[i][j]:
                mejora_arriba = True
                minimal[i][j] = minimal[i-1][j] + matrix[i][j]
    mejora_abajo = False
    for i in range(N-1):
        for j in range(N):
            if minimal[i][j] > minimal[i+1][j] + matrix[i][j]:
                mejora_abajo = True
                minimal[i][j] = minimal[i+1][j] + matrix[i][j]
    if all([not mejora_izquierda, not mejora_derecha, not mejora_arriba, not mejora_abajo]): break

print minimal[0][0]
