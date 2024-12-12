# 3. Напишите программу, которая считывает текст из файла 
#    (в файле может быть больше одной строки) 
#    и выводит в новый файл самое часто встречаемое слово в каждой строке 
#    и число – счётчик количества повторений этого слова в строке.

import collections

with open("./HW9/task3/text_for_task3.txt", "r") as file:
    content = file.read()
    file.close()

lines = [line for line in content.split("\n") if len(line) > 0]

result_dict = {}
for line in lines:
    words = line.lower().replace("\"", "").replace(",", "").replace("?", "").split(" ")
    words_dict = collections.Counter(words)
    key = max(words_dict, key=words_dict.get)
    print(f"{key}: {words_dict[key]}")
    result_dict[key] = words_dict[key]

with open("./HW9/task3/output_File_for_task3.txt", "w") as file:
    file.write(str(result_dict))