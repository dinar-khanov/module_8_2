def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_count = personal_sum(numbers)
        count = len(numbers) - incorrect_count
        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


# Примеры вызова функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # Передан не список
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Все корректно