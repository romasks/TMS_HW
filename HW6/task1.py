# Дан список чисел, отсортированных по возрастанию. 
# На вход принимается значение, равное одному из элементов списка.
# Реализовать функцию, выполняющую рекурсивный алгоритм бинарного поиска, 
# на выходе программа должна вывести позицию искомого элемента в исходном списке.

from random import randint

source_list = list(range(100))
print(source_list)

def binary_search(element, start, end):
    middle = (start + end) // 2
    if element == source_list[middle]:
        return middle
    elif element > source_list[middle]:
        return binary_search(element, middle + 1, end)
    else:
        return binary_search(element, start, middle)
    
searched_element = source_list[randint(0, len(source_list))]
print(searched_element)

print(binary_search(searched_element, 0, len(source_list)))
