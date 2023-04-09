import sys
import stddraw
from picture import Picture


def tile(file):
    n = int(input()) # высота
    m = int(input()) # ширина
    
    sourse = Picture('D:\python_projects\\anya_python\others\\filters\imgs\\4ksbnPYr1w8.jpg')
    S_H = sourse.height()
    S_W = sourse.width()

    small_picture = Picture(S_W // m, S_H // n)
    target = Picture(S_W, S_H)

    for colT in range(S_W // m):
        for rowT in range(S_H // n):
            colS = colT * (S_W) // ((S_W) // m)
            rowS = rowT * (S_H) // ((S_H) // n)
            # if rowS == 0:
            #     print(colS, colT)
            target.set(colT, rowT, sourse.get(colS, rowS))

    # for colT in range(S_W // m):
    #     for rowT in range(S_H // n):
    #         for i in range(n):
    #             for j in range(m):
    #                 target.set(colT + S_W // m * i, colS, small_picture.get(colT, rowT))


    stddraw.setCanvasSize(S_W, S_H)
    stddraw.picture(target)
    stddraw.show()

tile('fdlkj')
input()