from math import log
from numpy import euler_gamma


n = int(input())


def harmonicSmall(n):
    sum_ = sum([1/i for i in range(1, n)])
    return sum_


def harmocLarge(n):
    Hn = log(n) + euler_gamma + 1/(2 * n) - 1/(12 * n**2) - 1/(120 * n**4)
    return Hn


def harmonic(n):
    if n < 100:
        return harmonicSmall(n)
    else:
        return harmocLarge(n)


print(harmonic(n))
