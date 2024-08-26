from random import randint

lst = [randint(0, 100) for i in range(10)]
lst.sort()
print(*lst)

searched_element = lst[randint(0, len(lst))]
print(searched_element)

start = 0
middle = 0
end = len(lst)

while True:
    middle = (start + end) // 2

    if lst[middle] < searched_element:
        start = middle + 1
    elif lst[middle] > searched_element:
        end = middle
    else:
        break

print(f"index = {middle}")
    