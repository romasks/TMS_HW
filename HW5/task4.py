lst = [45,5,6,45,2,15,1,85,456,6,75]

sum = 0
min = lst[0]
max = lst[-1]

for n in lst:
    sum += n
    if n < min:
        min = n
    if n > max:
        max = n

print(f"sum = {sum}")
print(f"min = {min}")
print(f"max = {max}")
