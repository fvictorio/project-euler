from math import sqrt

def integer(n):
    return abs(n - round(n)) < 1E-5

def triangle_area(a, b, c):
    s = (a + b + c) / 2.0
    T = sqrt(s * (s - a) * (s - b) * (s - c))
    return T

#total = 0
#i = 3
#
#while True:
#    s = 3*i - 1
#    if s > 1000000000:
#        break
#    if integer(triangle_area(i, i, i-1)):
#        total += s
#        print(i)
#    s = 3*i + 1
#    if integer(triangle_area(i, i, i+1)):
#        total += s
#        print(i)
#    i += 2
#    if i > 100000: break

xs = [-5]
ys = [-8]

while True:
    x = xs[-1]
    y = ys[-1]

    xn = -2*x - y   - 1
    yn = -3*x - 2*y - 1

    s = (3*abs(xn)-1)/2
    if 2*s > 1000000000: break

    xs.append(xn)
    ys.append(yn)

total = 0
for x in xs:
    a = abs(x)
    if integer(triangle_area(a, a, a-1)):
        print(a)
        s = (3*a-1)
        assert(s <= 1000000000)
        total += s
    elif integer(triangle_area(a, a, a+1)):
        print(a)
        s = (3*a+1)
        assert(s <= 1000000000)
        total += s
    else:
        assert(False)

#xt = [-17]
#yt = [-30]
#
#while True:
#    x = xt[-1]
#    y = yt[-1]
#
#    xn = -2*x - y   + 1
#    yn = -3*x - 2*y + 1
#
#    s = (3*abs(xn)-1)/2
#    if s > 1000000000: break
#
#    xt.append(xn)
#    yt.append(yn)
