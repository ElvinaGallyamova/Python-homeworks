# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма

profit = float(input("Enter company's profit"))
costs = float(input("Enter company's costs "))
if profit > costs:
    print(f"The company works with profit. Profit is {profit / costs:.2f}")
else:
    print(f"The company works with costs. Profit is {costs / profit:.2f}")
