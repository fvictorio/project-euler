MAX_NUMBER = 99 
max_sum = [[0 for i in j] for j in triangle]
max_sum[len(triangle) - 1] = triangle[len(triangle) - 1]


for i in reversed(xrange(len(triangle) - 1)):
    for j in reversed(xrange(len(triangle[i]))):
        max_sum[i][j] = triangle[i][j] + max(max_sum[i+1][j], max_sum[i+1][j+1])



#def backtrack (i, j, sum_so_far):
#    global max_sum
#    sum_so_far += triangle[i][j]
#
#    #print "In row %i and col %i the sum is %i" % (i, j, sum_so_far)
#
#    if i + 1 == len(triangle):
#        return sum_so_far
#
#    if (sum_so_far + (len(triangle) - i - 1) * MAX_NUMBER) < max_sum:
#        return -1
#    
#    candidates = [j, j+1]
#    
#    for candidate in candidates:
#        possible_sum = backtrack(i + 1, candidate, sum_so_far)
#        if possible_sum == -1: 
#            continue
#        elif possible_sum > max_sum:

