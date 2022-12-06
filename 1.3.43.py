for i in range(1, 5000):
    for j in range(1, i):
        for k in range(j + 1, i):
            for u in range(k + 1 , i):
                for m in range(u + 1, i):
                    if (m**5 + j**5 + k**5 + u**5 == i**5):
                        print(j,"^5 + ",k,"^5 + ",u,"^5 + ",m,"^5 = ",i,"^5")