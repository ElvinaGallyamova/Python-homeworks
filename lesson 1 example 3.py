# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.

n = int(input("Enter the number: "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f'Total={total}')