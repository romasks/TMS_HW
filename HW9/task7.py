# 7. Дан текстовый файл с несколькими строками. 
# Зашифровать шифром Цезаря, при этом шаг зависит от номера строки: 
#   для первой строки шаг 1, для второй – 2 и т.д.
# Пример.
# Входные данные:
# Hello
# Hello
# Hello
# Hello
# Выходные данные:
# Ifmmp
# Jgnnq
# Khoor
# Lipps

import os

def shift(letter: str, shift: int) -> str:
    if ord(letter) in range(ord("A"), ord("Z")):
        return chr(((ord(letter) - ord("A")) + shift) % 24 + ord("A"))
    elif ord(letter) in range(ord("a"), ord("z")):
        return chr(((ord(letter) - ord("a")) + shift) % 24 + ord("a"))
    else:
        return letter

file_path = os.path.join(os.curdir, "HW9", "task7", "text.txt")

with open(file_path, "r") as file:
    content = file.read()
    file.close()

lines = content.split("\n")

for i in range(0, len(lines)):
    line = lines[i]
    print(''.join(list(map(lambda ch : shift(ch, i + 1), list(line)))))