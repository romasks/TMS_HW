from random import randint

lst = [5, 6, 7, 1, 2, 3, 4]

start = 0
for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        start = i

end = start - 1
start = start - len(lst)

searched_element = lst[randint(0, len(lst))]
print(searched_element)

middle = 0

while True:
    middle = (start + end) // 2
    print(f"middle = {middle}")

    if lst[middle] < searched_element:
        start = middle + 1
    elif lst[middle] > searched_element:
        end = middle
    else:
        break

print(f"index = {middle}")