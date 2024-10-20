# Сделать декоратор, который измеряет время, 
# затраченное на выполнение декорируемой функции.

from time import time

def calculate_fibonachi(input_func):
    def output_func(*args):
        number_of_numbers = args[0]
        start_time = time()
        input_func(number_of_numbers)
        execution_time = time() - start_time
        print(f"Execution time = {execution_time:.6f} seconds")
    return output_func

@calculate_fibonachi
def print_fibonachi(number_of_numbers):
    numbers = [1, 1]
    for i in range(2, number_of_numbers):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    print(numbers)

number_of_numbers = int(input("How much fibonachi numbers print? "))

calculate_fibonachi(print_fibonachi(number_of_numbers))
