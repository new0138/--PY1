salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0

for i in range(months):
    need = spend * (1 + increase) ** i - salary
    need_money += need

print(round(need_money))