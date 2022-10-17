salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

i = 1
while months >= i:
    i += 1
    a = spend - salary
    need_money += a
    spend *= (1 + increase)

print(round(need_money))
