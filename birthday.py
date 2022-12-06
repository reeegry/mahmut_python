import random

dict_ = {}
people_counter = 0

MONTH_31 = [1, 3, 5, 7, 8, 10, 12]
MONTH_30 = [4, 6, 9, 11]

leap_year = input("your year is leap year? [y/n]: ")
if leap_year == 'y':
    FEBRUARY = 29
else:
    FEBRUARY = 28

while True:
    person_month = random.randint(1, 12)

    if person_month in MONTH_31:
        person_day = random.randint(1, 31)
    elif person_month in MONTH_30:
        person_day = random.randint(1, 30)
    elif person_month == FEBRUARY:
        person_day = random.randint(1, FEBRUARY)

    if person_month in dict_ and dict_[person_month] == person_day:
        print(f"if took {people_counter + 1} people")
        break

    dict_[person_month] = person_day

    
    people_counter += 1



