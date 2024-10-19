# Программа получает на вход число H. 
# Реализовать функцию, которая определяет, 
# какие столбцы имеют хотя бы одно такое же число, 
# а какие не имеют (матрица M x N).

import matrix
from pprint import pprint

mx = matrix.create()
M = len(mx)
N = len(mx[0])

H = int(input("Enter number in range (0..100) to find inside matrix: "))

founded_row_number = -1

for m in range(M):
    for n in range(N):
        if mx[m][n] == H:
            founded_row_number = m
            break

pprint(mx)
if founded_row_number == -1:
    print(F"The number {H} not found in matrix")
else:
    print(f"The number {H} founded inside row {founded_row_number}")