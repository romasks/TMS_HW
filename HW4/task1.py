import math

a = int(input("Please, enter first variable = "))
b = int(input("Please, enter second variable = "))
x = int(input("Please, enter third variable = "))

a1 = a ** 2 + 4
r1 = a ** 2 / 3 + a1 / b + math.sqrt(a1) / 4 + math.sqrt(a1 ** 3) / 4

print("First formula:")
print("                  _______     ___________  ")
print("a*2   a*2 + 4   -/a*2 + 4   -/(a*2 + 4)*3  ")
print("--- + ------- + --------- + ------------- =", r1)
print(" 3       4          4             4        ")
print("")


r2 = (math.cos(x ** 2) ** 2 + math.sin(2 * x - 1) ** 2) ** (1 / 3)

print("Second formula:")
print("3 _____________________________ ")
print("-/ cos*2 (x*2) + sin*2 (2x - 1) =", r2)
print("")

r3 = math.cos(x) + math.sin(x)

print("Third formula:")
print("cos(x) + sin(x) =", r3)
print("")

r4 = 5 * x + 3 * x ** 2 + math.sqrt(1 + math.sin(x) ** 2)

print("Forth formula:")
print("           ______________  ")
print("5x + 3x2 -/ 1 + sin*2 (x) =", r4)
print("")
