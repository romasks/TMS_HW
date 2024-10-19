# Программа получает на вход строку – сообщение и указание, что нужно сделать: шифровать или дешифровать.
# Реализовать две функции: первая шифрует заданное сообщение шифром Цезаря, вторая – расшифровывает. 
# В зависимости от выбора пользователя (шифровать или дешифровать) вызывается соответствующая функция, 
# результат выводится в консоль.

shift = 3

def transform_char(ch, dest):
    base = ord('a')
    pos = ord(ch) - base
    res = (pos + shift * dest) % 26
    return chr(res + base)

def transform_string(msg, dest):
    return "".join([str(transform_char(ch, dest)) for ch in msg])

def crypt(msg):
    return transform_string(msg, 1)

def decrypt(msg):
    return transform_string(msg, -1)

message = input("сообщение: ")
operation = int(input("шифровать (0) или дешифровать (1) ? "))

if operation == 0:
    result = crypt(message)
    print(result)
elif operation == 1:
    result = decrypt(message)
    print(result)
else:
    print("невалидное значение")

