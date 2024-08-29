# Программа получает на вход два числа и находит их НОД (наибольший общий делитель). 
# Пример: на вход подаются числа 12 и 18, их НОД равен 6.

a = int(input("первое число: "))
b = int(input("второе число: "))

min = a if a < b else b
div = int(min / 2)

res = 1
for i in range(div, 1, -1):
    if a % i == 0 and b % i == 0:
        res = i
        break

print(f"НОД {a} и {b} = {res}")
