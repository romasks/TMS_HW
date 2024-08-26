"""
Дана строка. Замените в этой строке все появления буквы h на
букву H, кроме первого и последнего вхождения.
Подсказка: использовать метод replace с параметрами.
Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
"""

src_str = "hhhabchghhh"

index_of_first_h = src_str.find("h")
index_of_last_h = src_str.rfind("h")

left = index_of_first_h + 1
right = index_of_last_h
size = len(src_str)

dest_str = src_str[0:left] + src_str[left:right].replace("h", "H") + src_str[right:size]

print(dest_str)
