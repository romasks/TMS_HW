# Реализовать функцию, которая перемножает 
# элементы каждого столбца матрицы 
# с соответствующими элементами K-го столбца 
# (матрица M x N).

import matrix
from pprint import pprint

mx = matrix.create()
M = len(mx)
N = len(mx[0])

K = int(input("Enter row number to multiply with: "))

result_mx = []

for m in range(M):
    result_mx_row = []
    for n in range(N):
        result_mx_row.append(mx[m][n] * mx[K][n])
    result_mx.append(result_mx_row)

print("Result matrix:")
pprint(result_mx)