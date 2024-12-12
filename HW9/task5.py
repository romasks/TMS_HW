# 5. В текстовый файл построчно записаны фамилия и имя учащихся класса и оценка за контрольную. 
# Вывести на экран всех учащихся, чья оценка меньше трёх баллов.

import os

file_path = os.path.join(os.curdir, "HW9", "task5", "students.txt")

with open(file_path, "r") as file:
    students = file.read().split("\n")
    file.close()

students_dict = {student.split(" ")[0] + " " + student.split(" ")[1] : int(student.split(" ")[2]) for student in students}

result = {k: v for k, v in students_dict.items() if v < 3}

print("Студенты, чья оценка меньше трёх баллов:")
for student in result:
    print(student)