from math import log, exp, factorial


def binominal(k, n, p):
    log_k_n_f = 0
    for i in range(k + 1, n + 1):
        log_k_n_f += log(i)

    log_n_k_f = 0
    for i in range(1, n - k + 1):
        log_n_k_f += log(i)

    x = k * log(p) + (n - k) * log(1 - p) + log_k_n_f - log_n_k_f
    return(exp(x))


n = int(input())
p = float(input())
s = 0
for k in range(0, n + 1):
    s += binominal(k, n, p)

print(s)