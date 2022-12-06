m = int(input())
y = int(input())

M_CODES = [[4, 7], [1, 10], [5], [8], [2, 3, 11], [6], [12, 9]]
DAYS = {0: "Su", 1: "M", 2: "Tu", 3: "W", 4: "Th", 5: "F", 6: "St"}
MONTH_31 = [1, 3, 5, 7, 8, 10, 12]
MONTH_30 = [4, 6, 9, 11]
if y % 4==0 and y % 100 != 0 or y % 400 == 0:
    FEBRUARY = 29
else:
    FEBRUARY = 28

m_code = 0
for i in range(len(M_CODES)):
    if m in M_CODES[i]:
        m_code = i

y_code = (6 + y % 100 + (y % 100) // 4) % 7
day_code = (1 + y_code + m_code) % 7

if FEBRUARY == 29:
    day_code = (day_code - 1) % 7


def cal(index_first_day, days_count):
    c = [[_ for _ in range(7)] for _ in range(days_count // 7)]
    for i in range(days_count):
        c[index_first_day + (i // 7)][(index_first_day + i) % 7] = i        

    return c


if m in MONTH_31:
    days_list = cal(day_code, 31)
elif m in MONTH_30:
    days_list = cal(day_code, 30)
else:
    days_list = cal(day_code, FEBRUARY)


print(days_list)
