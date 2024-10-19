# Реализовать функцию, которая находит 
# сумму элементов матрицы (матрица M x N). 
#
# Определить, какую долю в общей сумме (процент) 
# составляет сумма элементов каждого столбца.
#

import matrix

mx = matrix.create()
M = len(mx)
N = len(mx[0])

sum = 0
row_sum_array = []

for m in range(M):
    row_sum = 0
    for n in range(N):
        row_sum += mx[m][n]
    sum += row_sum
    row_sum_array.append(row_sum)

print(f"Sum = {sum}")
print(f"Weight of rows sum: {[(row_sum / sum) * 100 for row_sum in row_sum_array]}")