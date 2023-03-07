import stddraw

def roadTo(x, y, x1, y1, n):
    for i in range(0, 21):
        if i > 0:
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.point((((i - 1) / 20) * (x1 - x) + x) / (n - 1), (((i / 20) * (y- 1) / 1 - y) + y) / (n - 1))
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.square(int((i - 1) / 20 * ((x1 - x) + y)) / (n - 1),
                           int((i - 1) / 20 * ((y1 - y) + y)) / (n - 1),
                           1 / (3 * (n - 1)))
        stddraw.setPenColor(stddraw.RED)
        stddraw.point(((i / 20) * (x1 - x) + x) / (n - 1), ((i / 20) * (y1 - y) + y) / (n - 1))
        stddraw.show(150)