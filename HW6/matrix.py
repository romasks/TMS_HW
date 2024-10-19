from random import randint
from pprint import pprint

def create():
    M = int(input("Enter number of rows: "))
    N = int(input("Enter number of columns: "))

    matrix = []
    for m in range(M):
        matrix.append([])
        for n in range(N):
            matrix[m].append(randint(0, 100))

    return matrix