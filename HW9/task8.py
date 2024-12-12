# 8. JSON и CSV.
# Исходные данные:
# https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2XnJDv9xN2LxusbE?usp=sharing
# Пункты задания:
# • Есть данные в формате JSON – взять с диска с исходными данными.
# • Реализовать функцию, которая считает данные из исходного JSON-файла и преобразует их в формат CSV
# • Реализовать функцию, которая сохранит данные в CSV-файл 
#   (данные должны сохраняться независимо от их количества – если добавить в исходный JSON-файл ещё одного сотрудника, 
#   работа программы не должна нарушаться).
# • Реализовать функцию, которая добавит информацию о новом сотруднике в JSON-файл. 
#   Пошагово вводятся все необходимые данные о сотруднике, формируются данные для записи.
# • Такая же функция для добавления информации о новом сотруднике в CSV-файл.
# • Реализовать функцию, которая выведет информацию об одном сотруднике по имени. Имя для поиска вводится с клавиатуры.
# • Реализовать функцию фильтра по языку: с клавиатуры вводится язык программирования, 
#   выводится список всех сотрудников, кто владеет этим языком программирования.
# • Реализовать функцию фильтра по году: ввести с клавиатуры год рождения, вывести средний рост всех сотрудников, 
#   у которых год рождения меньше заданного.
# • Программа должна представлять собой интерактив – пользовательское меню с возможностью выбора определённого действия 
#   (действия – функции из предыдущих пунктов + выход из программы). 
#   Пока пользователь не выберет выход из программы, должен предлагаться выбор следующего действия.

import json
import csv
import os

json_file_path = os.path.join(os.curdir, "HW9", "task8", "employees.json")
csv_file_path = os.path.join(os.curdir, "HW9", "task8", "employees.csv")

def readFromJsonFile() -> str:
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data

def getFieldNames(records: list) -> list:
    keys = list(dict(records[0]).keys())
    return keys

def writeToCsvFile(records: list, fields: list):
    with open(csv_file_path, "w") as csv_file:
        file_writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(fields)
        for record in records:
            # print(record)
            values = list(dict(record).values())
            file_writer.writerow(values)

def addNewRecord(fields: list) -> dict:
    record = dict()
    # print(fields)
    for field in fields:
        data = input(f"Enter {field}: ")
        # print(f"Field: {field}, value: {data}")
        try:
            record[field] = int(data)
        except ValueError:
            try:
                record[field] = float(data)
            except ValueError:
                if data == "True" or data == "False":
                    record[field] = data == "True"
                elif "," in data:
                    record[field] = data.replace(" ", "").split(",")
                else:
                    record[field] = data
    return record

def addRecordToJson(json_records: list, new_record: dict):
    data = json_records
    data.append(new_record)
    # print(data)
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def addRecordToCsv(new_record: dict):
    with open(csv_file_path, "a") as csv_file:
        file_writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        # print(new_record)
        values = list(dict(new_record).values())
        file_writer.writerow(values)

def getPersonFromJson(name: str, fields: list) -> dict:
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
        field_name = fields[0]
        for record in json_data:
            if name == record[field_name]:
                for field in fields:
                    print(f"{field}: {record[field]}")
    
def getPersonFromCsv(name: str, fields: list) -> dict:
    with open(csv_file_path, "r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        for row in csv_data:
            if name == row[0]:
                for i in range(0, len(fields)):
                    print(f"{fields[i]}: {row[i]}")

def searchByLanguage(records: list, lang_name: str):
    persons = []
    for record in records:
        if lang_name in list(record["languages"]):
            persons.append(record["name"])
    print(f"Persons: {', '.join(persons)}")

def calcAvgHeightByAge(records: list, year: int):
    persons = []
    for record in records:
        person_year = int(record["birthday"].split(".")[2])
        if year > person_year:
            persons.append(int(record["height"]))
    print(f"There are {len(persons)} person(s) younger than {year} with average height {sum(persons) / len(persons)} cm")

# json_records = readFromJson()
# fields = getFieldNames(json_records)
# writeToCsv(json_records, fields)

# new_record = addNewRecord(fields)
# print(new_record)
# addRecordToJson(json_records, new_record)
# addRecordToCsv(json_records, new_record)

# person_name = input("Enter person name: ")
# getPersonFromJson(person_name, fields)
# getPersonFromCsv(person_name, fields)

# lang_name = input("Enter programming language name: ")
# searchByLanguage(json_records, lang_name)

# year = int(input("Enter birth year: "))
# calcAvgHeightByAge(json_records, year)

json_records = []
fields = []
choice = -1
while choice != 0:
    print()
    print("Please, choose the option from menu:")
    print("1 -- read data from json file")
    print("2 -- store data in csv file")
    print("3 -- add new person's details into json file")
    print("4 -- add new person's details into csv file")
    print("5 -- get person's info by name")
    print("6 -- filter persons by programing language")
    print("7 -- calculate average height of older persons")
    print("8 -- print data")
    print("0 -- exit program")
    choice = int(input("Enter your choice: "))

    if choice in range(2, 8) and len(json_records) == 0:
        print("Read data from json file first")
        input()
    elif choice == 0:
        break
    elif choice == 1:
        json_records = readFromJsonFile()
        fields = getFieldNames(json_records)
    elif choice == 2:
        writeToCsvFile(json_records, fields)
    elif choice == 3:
        new_record = addNewRecord(fields)
        addRecordToJson(json_records, new_record)
    elif choice == 4:
        new_record = addNewRecord(fields)
        addRecordToCsv(json_records, new_record)
    elif choice == 5:
        person_name = input("Enter person name: ")
        getPersonFromJson(person_name, fields)
    elif choice == 6:
        lang_name = input("Enter programming language name: ")
        searchByLanguage(json_records, lang_name)
    elif choice == 7:
        year = int(input("Enter birth year: "))
        calcAvgHeightByAge(json_records, year)
    elif choice == 8:
        for record in json_records:
            print(record)
    else:
        print("There are no that choice")
