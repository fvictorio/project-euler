fifth = lambda x: x**5

def is_sum_of_fifths (n):
    return n == sum(map(fifth,map(int,str(n))))

