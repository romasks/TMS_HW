# Программа получает на вход число. 
# Реализовать функцию, которая определяет, является ли это число простым 
# (делится только на единицу и на само себя).

input_number = int(input("число: "))

def is_primary(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(f"is {input_number} primary? {is_primary(input_number)}")
