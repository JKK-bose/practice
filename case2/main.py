import datetime


# Функция для определения дня недели
def day_of_week(day, month, year):
    date_obj = datetime.datetime(year, month, day)
    return date_obj.strftime("%A")


# Функция для определения високосного года
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Функция для определения возраста пользователя
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


# Функция для форматированного вывода даты в звездочках
def format_date_with_stars(day, month, year):
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    year_str = str(year)
    formatted_date = day_str.replace('0', '*') + ' ' + month_str.replace('0', '*') + ' ' + year_str.replace('0', '*')
    return formatted_date


# Основная программа
def main():
    # Запрос данных у пользователя
    day = int(input("Введите день вашего рождения (число): "))
    month = int(input("Введите месяц вашего рождения (число): "))
    year = int(input("Введите год вашего рождения (число): "))

    # Определение дня недели
    day_name = day_of_week(day, month, year)
    print(f"День вашего рождения был в {day_name}.")

    # Проверка на високосный год
    if is_leap_year(year):
        print(f"Год {year} был високосным.")
    else:
        print(f"Год {year} не был високосным.")

    # Вычисление и вывод возраста пользователя
    birth_date = datetime.date(year, month, day)
    age = calculate_age(birth_date)
    print(f"Вам сейчас {age} лет.")

    # Вывод даты рождения в формате с звездочками
    formatted_date = format_date_with_stars(day, month, year)
    print(f"Дата вашего рождения в формате звёздочек: {formatted_date}")


if __name__ == "__main__":
    main()