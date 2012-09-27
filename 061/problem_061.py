from itertools import count

if 0:
    polygonal = [ [] for i in xrange(9) ]
    
    for i in count(10):
        n3 = (i * (i + 1)) / 2
        n4 = i**2
        n5 = (i * (3*i - 1)) / 2
        n6 = (i * (2*i - 1))
        n7 = (i * (5*i - 3)) / 2
        n8 = (i * (3*i - 2))

        if 1000 <= n3 < 10000: polygonal[3].append(n3)
        if 1000 <= n4 < 10000: polygonal[4].append(n4)
        if 1000 <= n5 < 10000: polygonal[5].append(n5)
        if 1000 <= n6 < 10000: polygonal[6].append(n6)
        if 1000 <= n7 < 10000: polygonal[7].append(n7)
        if 1000 <= n8 < 10000: polygonal[8].append(n8)

        if (n3 >= 10000) and (n4 >= 10000) and (n5 >= 10000) and (n6 >= 10000) and (n7 >= 10000) and (n8 >= 10000): 
            break 

if 0:
    next = [ {} for i in xrange(9) ]

    for i in xrange(3,9):
        for m in polygonal[i]:
            next[i][m] = []
            sm = str(m)
            for j in xrange(3,9):
                if i == j: continue
                for n in polygonal[j]:
                    sn = str(n)
                    if sm[2:4] == sn[0:2]:
                        next[i][m].append( (j, n) )

# and (str(conj[5])[2:4] == str(conj[0])[0:2])
def backtrack (i, m, conj, used):
    if (len(conj) == 6) and (str(conj[5])[2:4] == str(conj[0])[0:2]):
    #if all(used):
        print "Foooooooooooound:"
        print conj
        return True

    #print "%s i = %i m = %i" % ("-" * len(conj), i, m)

    for j, n in next[i][m]:
        if used[j]: continue

        #print "%s j = %i n = %i" % ("*" * len(conj), j, n)
        
        if backtrack(j, n, conj + [n], used[:j] + [True] + used[j+1:]): return True
        
    #print conj
    return False
