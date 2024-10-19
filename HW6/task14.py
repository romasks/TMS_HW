# Дана матрица M x N. Исходная матрица состоит из нулей и единиц. 
# Реализовать функцию, которая добавит к матрице ещё один столбец, 
# элементы которого делает количество единиц в соответствующей строке чётным.

from random import randint
from pprint import pprint

M = int(input("Enter number of rows: "))
N = int(input("Enter number of columns: "))

matrix = []
for m in range(M):
    matrix.append([])
    for n in range(N):
        matrix[m].append(randint(0, 1))

pprint(matrix)

for m in range(M):
    if sum(matrix[m]) % 2 == 1:
        matrix[m].append(1)
    else:
        matrix[m].append(0)

pprint(matrix)
