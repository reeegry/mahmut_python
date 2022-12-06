n = int(input())
count = 0

for i in range(1, int(n**1/3)):
    for j in range(i , int(n**1/3)):
        for k in range(1, int(n**1/3)):
            for u in range(k, int(n**1/3)):
                if i**3 + j**3 == k**3 + u**3 == n:
                    print(i, j, "\n", k, u, n)
                    count += 1
                if count > 2:
                    break
