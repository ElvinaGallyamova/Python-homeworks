#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        arg1 = int(input("Enter dividend"))
        arg2 = int(input("Enter divider"))
        res = arg1/arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero as a divider"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Divider can't be zero")

print(f'result  {div()}')