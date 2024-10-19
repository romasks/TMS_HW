# Реализовать функцию, которая находит 
# сумму элементов на главной диагонали 
# и сумму элементов на побочной диагонали 
# (матрица M x N).

import matrix
from pprint import pprint

mx = matrix.create()
M = len(mx)
N = len(mx[0])

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for m in range(M):
    for n in range(N):
        if m == n:
            primary_diagonal_sum += mx[m][n]
        elif n == N - m - 1:
            secondary_diagonal_sum += mx[m][n]

pprint(mx)

print(f"Sum of numbers on the primary diagonal: {primary_diagonal_sum}")
print(f"Sum of numbers on the secondary diagonal: {secondary_diagonal_sum}")