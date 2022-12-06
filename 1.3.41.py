import random

n = int(input())
#doors = [1, 2, 3]
count_stay = 0
count_switched = 0

for i in range(n):
    prize = random.randint(0, 2)
    chose = random.randint(0, 2)
    #opened_door = doors[prize - random.randint(0, 1)]
    if prize == chose:
        count_stay += 1
    else:
        count_switched += 1

print("win count then swith:", count_switched, \
    "\nwin count then save chose:", count_stay)

if count_switched > count_stay:
    print("probability of win then switch bigger:", count_switched / (count_switched + count_stay))
else:
    print("probability then stay bigger:", count_stay / (count_stay + count_switched))
    


