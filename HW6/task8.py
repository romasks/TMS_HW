# Реализовать функцию, которая находит минимальный и 
# максимальный элементы в матрице (матрица M x N). 
# Вывести в консоль индексы найденных элементов.

import matrix
from pprint import pprint

mx = matrix.create()
pprint(mx)

elems_dict = {}
M = len(mx)
N = len(mx[0])
for m in range(M):
    for n in range(N):
        elem = mx[m][n]
        elems_dict[elem] = (m, n)

keys = list(elems_dict.keys())
keys.sort()
print(keys)

min_elem = elems_dict[keys[0]]
max_elem = elems_dict[keys[-1]]

pprint(f"Min element located at [{min_elem[0]},{min_elem[1]}]")
pprint(f"Max element located at [{max_elem[0]},{max_elem[1]}]")
