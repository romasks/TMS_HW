"""
Дан прямоугольный треугольник с катетами cat_a и cat_b. Найти
площадь треугольника и его гипотенузу.
"""

import math

cat_a = 5
cat_b = 7

print("cat_a =", cat_a)
print("cat_b =", cat_b)
print("Square = ", cat_a * cat_b / 2)
print("hypoten = ", math.sqrt(cat_a ** 2 + cat_b **2 ))