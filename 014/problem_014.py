import time

lengths = {1:1}

LIMIT = 1000000

def chain_length(nn):
    n = nn
    length = 1
    pase_por_aca = []
    while True:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        if lengths.has_key(n):
            for i in pase_por_aca:
                lengths[i] += lengths[n]
            lengths[nn] = lengths[n] + length
            return lengths[n] + length
        else:
            if n <= LIMIT:
                pase_por_aca.append(n)
                lengths[n] = 0
            for i in pase_por_aca:
                lengths[i] += 1
        length += 1

if 1:
    begin = time.time()
    max_length = 1
    number_with_max_length = 1
    for i in xrange(2,LIMIT+1):
        i_length = chain_length(i)
        if i_length > max_length:
            max_length = i_length
            number_with_max_length = i
    end = time.time()
    print end - begin
    print number_with_max_length
