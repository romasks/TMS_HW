"""
Дано трехзначное число, найти сумму его цифр. Например,
дано 123 – сумма 6, дано 555, сумма 15.
"""

test_int_1 = 123
test_int_2 = 555

def print_digits_sum(test_int):
    first_digit = test_int // 100
    second_digit = test_int // 10 % 10
    third_digit = test_int % 10
    print("Sum of ", test_int, " is ", (first_digit + second_digit + third_digit))

print_digits_sum(test_int_1)
print_digits_sum(test_int_2)
