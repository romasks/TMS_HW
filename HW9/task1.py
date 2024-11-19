# 1.Работа с модулем os
# Есть папка, в которой лежат файлы с разными расширениями.
# Программа должна:
# • Вывести имя вашей ОС
# • Вывести путь до папки, в которой вы находитесь
# • Рассортировать файлы по расширениям, например, для текстовых файлов создается папка, 
#   в неё перемещаются все файлы с расширением .txt, то же самое для остальных расширений
# • После рассортировки выводится сообщение типа «в папке с текстовыми файлами перемещено 5 файлов, 
#   их суммарный размер – 50 гигабайт»
# • Как минимум один файл в любой из получившихся поддиректорий переименовать. 
#   Сделать вывод сообщения типа «Файл data.txt был переименован в some_data.txt»
# • Программа должна быть кроссплатформенной – никаких хардкодов с именем диска и слэшами.

import os

print(os.name)

try:
    path = os.path.join(".", "HW9", "task1", "test_folder")
    os.chdir(path)
except FileNotFoundError as e:
    print(e)
cur_dir = os.getcwd()
# print(cur_dir)

files = os.listdir(cur_dir)
for file in files:
    if os.path.isfile(file):
        ext = file.split(".")[1]
        if os.path.exists(ext) == False:
            os.mkdir(ext)
        os.replace(file, os.path.join(ext, file))
# print(files)

dirs = os.listdir(cur_dir)
# print(dirs)

def get_dir_size(path: str) -> int:
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
    
for dir in dirs:
    dir_path = os.path.join(os.getcwd(), dir)
    num_files = len(os.listdir(dir_path))
    dir_size = get_dir_size(dir_path)
    print(f"В папку {dir} перемещено {num_files} файлов, их суммарный размер – {dir_size}")

for dir in dirs:
    if dir == "txt":
        file = os.listdir(dir)[0]
        os.replace(os.path.join(dir, file), os.path.join(dir, "new_" + file))
        print(f"Файл {file} был переименован в new_{file}")