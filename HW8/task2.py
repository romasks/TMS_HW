# Реализовать программу с функционалом калькулятора 
# для операций над двумя числами. 
# Числа и операция вводятся пользователем с клавиатуры. 
# Использовать ООП. 
# Использовать обработку исключений.

def calculate(a: int, b: int, operation: str) -> float:
    if operation == "+":
        res = a + b
    elif operation == "-":
        res = a - b
    elif operation == "*":
        res = a * b
    elif operation == "/":
        res = a / b
    else:
        raise Exception("Неизвестная операция")
    return res

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Введите символ операции: ")
    res = calculate(a, b, operation)
    print(f"Результат операции {a} {operation} {b} равняется {res}")
except ZeroDivisionError:
    print("Делить на 0 нельзя")
except ValueError as e:
    print("Необходимо ввести целое значение! ", e)
except Exception as e:
    print(e)



