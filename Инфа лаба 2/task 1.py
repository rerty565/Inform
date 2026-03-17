money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget_st=money_capital+salary
kol=0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend<budget_st:
    budget_st=salary+money_capital
    spend=spend+(spend*increase)
    money_capital=money_capital-(spend-salary)
    kol+=1
print("Количество месяцев, которое можно протянуть без долгов:", kol)
