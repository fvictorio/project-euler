def is_solution (a, b, p):
    return (a**2+b**2 == (p-a-b)**2)

def get_solutions(p):
    solutions = 0
    for a in xrange(1,p/2):
        for b in xrange(1,a+1):
            if is_solution(a,b,p):
                solutions += 1
    return solutions
