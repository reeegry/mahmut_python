import stddraw
import stdarray

n = 20
color = stddraw.BLUE

a = stdarray.create2D(n, n, False)
x = n // 2
y = n // 2

k = 10000
while k:
    k -= 1
    stddraw.setPenColor(color)
    stddraw.square(x, y, 1 / (3 * (n - 1)))

help(stddraw)