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

# Функция для форматированного вывода цифры в виде звездочек (5 строк)
def digit_to_stars(digit):
    digit_patterns = {
        '0': ['*****', '*   *', '*   *', '*   *', '*****'],
        '1': ['  *  ', ' **  ', '  *  ', '  *  ', '*****'],
        '2': ['*****', '    *', '*****', '*    ', '*****'],
        '3': ['*****', '    *', '*****', '    *', '*****'],
        '4': ['*   *', '*   *', '*****', '    *', '    *'],
        '5': ['*****', '*    ', '*****', '    *', '*****'],
        '6': ['*****', '*    ', '*****', '*   *', '*****'],
        '7': ['*****', '    *', '    *', '    *', '    *'],
        '8': ['*****', '*   *', '*****', '*   *', '*****'],
        '9': ['*****', '*   *', '*****', '    *', '*****']
    }
    return digit_patterns.get(digit, ['     ']*5)

# Функция для форматированного вывода даты в звездочках
def format_date_with_stars(day, month, year):
    date_str = f"{day:02d}{month:02d}{year}"
    
    # Создаем список из 5 строк (по количеству строк в каждой цифре)
    lines = [""] * 5
    
    for char in date_str:
        digit_stars = digit_to_stars(char)
        for i in range(5):
            lines[i] += digit_stars[i] + " "
    
    # Добавляем разделители между день/месяц/год
    formatted_lines = []
    for line in lines:
        # Вставляем пробелы после дня и месяца
        formatted_line = line[:12] + " " + line[12:24] + " " + line[24:]
        formatted_lines.append(formatted_line)
    
    return "\n".join(formatted_lines)

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
    print("Дата вашего рождения в формате звёздочек:")
    print(format_date_with_stars(day, month, year))

if __name__ == "__main__":
    main()
