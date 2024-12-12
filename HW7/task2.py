# Дан список чисел. С помощью filter() получить 
# список тех элементов из исходного списка, 
# значение которых больше 0.

from random import randint

numbers = [randint(-100, 100) for i in range(20)]
print(numbers)

result = [i for i in numbers if i > 0]
print(result)