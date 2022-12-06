from re import A


n = int(input())


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a        
    return a


eulers_func_value = 1
for i in range(2, n):
    if gcd(i, n) == 1:
        eulers_func_value += 1

print(eulers_func_value)
