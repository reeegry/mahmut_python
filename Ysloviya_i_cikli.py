from random import random


num = input()
sqrt_num = str(int(num)**2)
print(num, sqrt_num, len(sqrt_num)//2, len(num), len(num) % 2)
if sqrt_num[len(sqrt_num)//2 - len(num)//2] != '0':
    random_int = sqrt_num[len(sqrt_num)//2 - len(num)//2:len(sqrt_num)//2 + len(num)//2 + len(num) % 2]
else:
    random_int = sqrt_num[len(sqrt_num)//2 - len(num)//2 + 1:len(sqrt_num)//2 + len(num)//2 + len(num) % 2 + 1]
print(random_int)