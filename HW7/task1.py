# Дан список чисел. С помощью map() получить список, 
# где каждое число из исходного списка переведено в строку.
# Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]

from random import randint

numbers = [randint(0, 100) for i in range(20)]
print(numbers)

result = [str(i) for i in numbers]
print(result)