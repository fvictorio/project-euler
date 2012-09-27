#matrix = [[131, 673, 234, 103, 18],
#          [201, 96, 342, 965, 150],
#          [630, 803, 746, 422, 111],
#          [537, 699, 497, 121, 956],
#          [805, 732, 524, 37, 331]]
matrix = open('matrix.txt').readlines()
matrix = [[int(i) for i in j[:-2].split(',')] for j in matrix]

N = len(matrix)
minimal = [[0 for i in j] for j in matrix]

for i in range(N):
    minimal[i][N-1] = matrix[i][N-1]

for j in reversed(range(N-1)):
    for i in range(N):
        v = [-1] * N
        v[i] = matrix[i][j]
        ii = i-1
        while ii >= 0:
            v[ii] = matrix[ii][j] + v[ii+1]
            ii -= 1
        ii = i+1
        while ii < N:
            v[ii] = matrix[ii][j] + v[ii-1]
            ii += 1
        for ii in range(N):
            v[ii] += minimal[ii][j+1]
        minimal[i][j] = min(v)

print min(i[0] for i in minimal)
