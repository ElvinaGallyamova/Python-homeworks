# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = float(input("Enter company's profit"))
costs = float(input("Enter company's costs "))
if profit > costs:
    print(f"The company works with profit. Profit is {profit / costs:.2f}")
    workers = int(input("Enter the quantity of company workers "))
    print(f"The profit for one worker is  {profit / workers:.2f}")
elif profit == costs:
    print("The company is working at zero")
else:
    print("The company is working at a loss")
