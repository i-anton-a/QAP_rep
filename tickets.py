ticket = int(input('Сколько билетов будете брать?'))
age = [int(input('Сколько вам лет ')) for i in range(ticket)]
sum_total = 0
sum1 = 990
sum2 = 1390
sum_ticket1 = 0
sum_ticket2 = 0

for i in range(len(age)):
    if 18 <= age [i] <= 25:
        sum_ticket1 += 1
    if age [i] > 25:
        sum_ticket2 += 1

if ticket > 3:
    sum_total = (sum1 * sum_ticket1 + sum2 * sum_ticket2) - (sum1 * sum_ticket1 + sum2 * sum_ticket2)*0.1
else:
    sum_total = (sum1 * sum_ticket1 + sum2 * sum_ticket2)

print("Количество билетов : ", ticket, "По цене : ", sum_total)
