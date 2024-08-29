# Программа получает на вход число в десятичной системе счисления. 
# Реализовать функцию, которая переводит входное число в двоичную систему счисления. 
# Допускается реализация функции как в рекурсивном варианте, так и с итеративным подходом.

number_10 = int(input("число в десятичной системе счисления: "))
print(number_10)

def to_binary(number):
    tail = number & 1
    print(f'tail = {tail}')

    head = number >> 1
    print(f'head = {head}')

    if head == 0:
        return str(tail)
    else:
        return to_binary(head) + str(tail)

print(to_binary(number_10))
