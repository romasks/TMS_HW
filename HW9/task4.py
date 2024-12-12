# 4. Напишите программу, которая получает на вход строку с названием текстового файла 
# и выводит на экран содержимое этого файла, заменяя все запрещённые слова звездочками.
# Запрещённые слова, разделённые символом пробела, должны храниться в файле stop_words.txt.
# Программа должна находить запрещённые слова в любом месте файла, даже в середине другого слова. 
# Замена независима от регистра: если в списке запрещённых есть слово exam, то замениться должны exam, eXam, EXAm и другие вариации.
# Пример.
# в stop_words.txt записаны слова: hello email python the exam wor is
# Текст файла для цензуры выглядит так: 
# Hello, World! Python IS the programming language of thE future. My EMAIL is... PYTHON as AwESOME!
# Тогда итоговый текст: 
# *****, ***ld! ****** ** *** programming language of *** future. My ***** **... ****** ** awesome!!!!

import os

folders = input("Enter folder separated by space where file located: ")
file_name = input("Enter file name: ")

path = os.curdir
for dir in folders.split(" "):
    path = os.path.join(path, dir)
path = os.path.join(path, file_name)
print(path)

file_exists = os.path.exists(file_name)
print(f"Exists: {file_exists}")

with open(path, "r") as file:
    content = file.read()
    file.close()

with open(os.path.join(os.curdir, "HW9", "task4", "stop_words.txt"), "r") as file:
    stop_words = file.read().split(" ")
    file.close()

for word in stop_words:
    mask = ''.join(["*" for i in range(0, len(word))])
    content = content.replace(word, mask)

print(content)