# 6. В файл записано некоторое содержимое (буквы, цифры, пробелы, специальные символы и т.д.). 
# Числом назовём последовательность цифр, идущих подряд. Вывести сумму всех чисел, записанных в файле.
# Пример.
# Входные данные: 123 ааа456 1x2y3z 4 5 6
# Выходные данные: 600

import os
import re

file_path = os.path.join(os.curdir, "HW9", "task6", "text.txt")

with open(file_path, "r") as file:
    content = file.read()
    file.close()

numbers = re.findall(r'\d+', content)
numbers = list(map(lambda x: int(x), numbers))

print(sum(numbers))