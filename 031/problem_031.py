#coins = [1,2,5,10,20,50,100,200]

def how_many_ways (n,coins):
    coins = [i for i in coins if i <= n]
    coins.sort()
    coins.reverse()

    if n < 0: 
        total_ways = 0
    if (n == 0) or ((len(coins) == 1) and (n % coins[0] == 0)): # trivial
        total_ways = 1
    else:
        total_ways = 0

        for i in xrange(len(coins)):
            resto = n - coins[i]
            coins_used = coins[i:]
            total_ways += how_many_ways(resto,coins_used)
#            print "how_many_ways(%i, " % resto
#            print coins_used
#            print ")"

    return total_ways

#    print "Computing ways of %i using:" % n
#    print coins
#    print "is %i" % total_ways
#    print ""
