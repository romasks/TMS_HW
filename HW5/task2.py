N = int(input("Стоимость телефона: "))
k = int(input("Сумма ежедневного накопления: "))

saved_money = 0
count_of_days = 0
day_of_week = 1

while saved_money < N:
    count_of_days += 1

    if day_of_week == 7:
        day_of_week = 1
    else:
        day_of_week += 1
        saved_money += k

print(f"Кол-во дней для накопления суммы: {count_of_days}")