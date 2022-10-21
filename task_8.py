money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

delta = spend - salary
while (money_capital - delta) >= spend:
    spend *= (1 + increase)
    delta = spend - salary

    if delta >= (spend - money_capital):
        month += 1

# TODO Оформить решение

print(month)
