
chose = int(input("input: 1 - if you want to convert from grigoryan calendar to julian \
                0 - from julian to grigoryan"))

day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))

a = (14 - month) // 12
y = year + 4800 - a
m1 = month + 12 * a - 3

if chose:
    jdn = day + (153 * m1 + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    c = jdn + 32082
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m2 = (5 * e + 2) // 153

    day_j = e - (153 * m2 + 2) // 5 + 1
    mounth_j = m2 + 3 - 12*(m2 // 10)
    year_j = d - 4800 + m2 // 10

    print(day_j,".", mounth_j,".", year_j)
else:
    jdn = day + (153 * m1 + 2) // 5 + 365 * y + y // 4 - 32083

    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m2 = (5 * e + 2) // 153

    day_g = e - (153 * m2 + 2) // 5 + 1
    mounth_g = m2 + 3 - 12 * (m2 // 10)
    year_g = 100 * b + d - 4800 + (m2 // 10)

    print(day_g,".",mounth_g,".",year_g)

