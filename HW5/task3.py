count_of_numbers = int(input("Сколько чисел Фибоначчи вывести? "))

fibonachi_numbers = [1, 1]

while len(fibonachi_numbers) < count_of_numbers:
    fibonachi_numbers.append(fibonachi_numbers[-1] + fibonachi_numbers[-2])

print("Последовательность:")
print(*fibonachi_numbers, sep=" ")