# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Enter time in seconds"))
time_in_hours: int = time_in_seconds // 3600
time_in_minutes: int = (time_in_seconds - time_in_hours * 3600) // 60
time_in_sec2: int = time_in_seconds - (time_in_hours * 3600 + time_in_minutes * 60)
print(f"Time in the format hh:mm:ss, {time_in_hours}:{time_in_minutes}:{time_in_sec2}")