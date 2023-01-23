# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.

n = (int(input("Enter positive number ")))
max_number = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_number:
        max_number = n % 10
    if n > 9:
        continue
    else:
        print("Мax numeral in number is  ", max_number)
        break
        