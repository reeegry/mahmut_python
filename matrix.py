raws_amount = int(input())
columns_amount = int(input())

matrix = [[0 for i in range(raws_amount + 2)] for j in range(columns_amount + 2)]

print(matrix)

for i in range(1, columns_amount + 1):
    print(f"input {i} column")
    for j in range(1, raws_amount + 1):
        matrix[i][j] = int(input())

indexes = []

def recur(i, j):

    if str(i + 1) + str(j) not in indexes and 0 < i < columns_amount + 1 and 0 < j < raws_amount + 1 and matrix[i + 1][j] == matrix[i][j]:
        indexes.append(str(i + 1) + str(j))
        recur(i + 1, j)
    if str(i) + str(j + 1) not in indexes and 0 < i < columns_amount + 1 and 0 < j < raws_amount + 1 and matrix[i][j + 1] == matrix[i][j]:
        indexes.append(str(i) + str(j + 1))
        recur(i, j + 1)
    if str(i - 1) + str(j) not in indexes and 0 < i < columns_amount + 1 and 0 < j < raws_amount + 1 and matrix[i - 1][j] == matrix[i][j]:
        indexes.append(str(i - 1) + str(j))
        recur(i - 1, j)
    if str(i) + str(j - 1) not in indexes and 0 < i < columns_amount + 1 and 0 < j < raws_amount + 1 and matrix[i][j - 1] == matrix[i][j]:
        indexes.append(str(i) + str(j - 1))
        recur(i, j - 1)
    
    return len(set(indexes))
    

max_ = 0

for i in range(1, columns_amount):
    for j in range(1, raws_amount):
        indexes = []
        temp_max = recur(i, j)
        max_ = max(temp_max, max_)

print(max_)

k = 0
for i in range(1, raws_amount + 1):
    for j in range(1, columns_amount + 1):
        k += 1
        if k == columns_amount:
            print(matrix[j][i])
            k = 0
        else:
            print(matrix[j][i], end=' ')

#----------------------

matrix_str = [[str(matrix[j][i]) for i in range(0, raws_amount + 2)] for j in range(0, columns_amount + 2)]


print(matrix_str)

k = 0
for i in range(1, raws_amount + 1):
    for j in range(1, columns_amount + 1):
        k += 1
        if not (str(j) + str(i) in indexes):
           matrix_str[j][i] = '*'
            
        if k == columns_amount:
            print(matrix_str[j][i])
            k = 0
        else:
            print(matrix_str[j][i], end=' ')




