import math

x = int(input("Enter number: "))

n = 10

sin_x = 0
cos_x = 0

for i in range(n):
    print(f"top = {(x ** (2 * i))}")
    print(f"bottom = {math.factorial(2 * i)}")

    sin_x += (((-1) ** i) * (x ** (2 * i + 1))) / math.factorial(2 * i + 1)
    cos_x += (((-1) ** i) * (x ** (2 * i))) / math.factorial(2 * i)

print(f"sin(x) = {sin_x:.10f}")
print(f"cos(x) = {cos_x:.10f}")