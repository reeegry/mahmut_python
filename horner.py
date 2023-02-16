from math import exp, factorial

x = int(input())
n = int(input())

a = [int(i) for i in input().split()]

def evaluate(x1, coefs):
    ans = coefs[0] * x1 + coefs[1]   
    n = len(coefs)
    for i in range(2, n):
        ans = ans * x1 + coefs[i]

    return ans


def expt(x,n):
    e_x_coef = [1]
    fact = e_x_coef[0]
    for i in range(1, n + 1):
        fact = fact * i
        e_x_coef.append(1/fact)
    return evaluate(x, e_x_coef[::-1])


print(expt(x, n))
print(exp(x))