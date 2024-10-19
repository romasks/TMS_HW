# Реализовать функцию, которая суммирует 
# элементы каждой строки матрицы 
# с соответствующими элементами L-й строки 
# (матрица M x N).

import matrix
from pprint import pprint

mx = matrix.create()
M = len(mx)
N = len(mx[0])

L = int(input("Enter row number to sum with: "))

result_mx = []

for m in range(M):
    result_mx_row = []
    for n in range(N):
        result_mx_row.append(mx[m][n] + mx[L][n])
    result_mx.append(result_mx_row)

print("Result matrix:")
pprint(result_mx)