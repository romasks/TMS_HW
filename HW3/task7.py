"""
Дано трехзначное число, найти количество его десятков.
Например, дано 123 – количество десятков: 2, дано 978 –
количество десятков: 7.
"""

test_int_1 = 123
test_int_2 = 978

def print_middle_digit(test_int):
    print("Middle of ", test_int, " is ", (test_int // 10 % 10))

print_middle_digit(test_int_1)
print_middle_digit(test_int_2)
