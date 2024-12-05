money_capital = 20000 # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = 0 #
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0 :
    if money_capital < spend - salary :
        break
    money_capital -= spend - salary
    spend *= 1 + increase
    i += 1
print("Количество месяцев, которое можно протянуть без долгов:", i)



