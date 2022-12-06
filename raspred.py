from math import log, exp, factorial


def binominal(k, n, p):
    x = k * log(p) + (n - k) * log(1 - p) + log(factorial(n)) - log(factorial(k)) - log(factorial(n - k))
    return(exp(x))


n = 2000
s = 0
for i in range(0, n + 1):
    s += binominal(i, n, 0.4)

print(s)