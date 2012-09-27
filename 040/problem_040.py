irrational = ''
for i in xrange(1,1000001):
    irrational += str(i)

print(int(irrational[0]) * int(irrational[9]) * int(irrational[99]) * int(irrational[999]) * int(irrational[9999]) * int(irrational[99999]) * int(irrational[999999]))
