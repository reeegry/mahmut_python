n = int(input())
x = int(input())

a = [int(i) for i in input().split()]
b = a[0] * x + a[1]
for i in range(2, len(a)):
    b = b * x + a[i]

print(b)
