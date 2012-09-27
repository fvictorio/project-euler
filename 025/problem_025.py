LEN = 1000

if 1:
    fib1 = 1
    fib2 = 1
    i = 2
    while True:
        if len(str(fib2)) == LEN:
            print i
            break
        nextfib = fib1 + fib2
        (fib1, fib2) = (fib2, nextfib)
        i += 1
