# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, work_time, salary, bonus = argv

try:
    work_time = float(work_time)
    salary = int(salary)
    bonus = int(bonus)
    result = (work_time * salary) + bonus
    print (f'Заработная плата сотрудника составила: {result}')
except ValueError:
    print('Not a number')