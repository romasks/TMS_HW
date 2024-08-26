"""
Дано целое число. Выведите его последнюю цифру.
Например, дано 200 - последняя цифра 0. Дано 123 - последняя
цифра 3. Дано 587 - последняя 7.
"""

test_int_1 = 200
test_int_2 = 123
test_int_3 = 587

def print_last_digit(test_int):
    print("Last of ", test_int, " is ", (test_int % 10))

print_last_digit(test_int_1)
print_last_digit(test_int_2)
print_last_digit(test_int_3)
