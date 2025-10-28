"""
Задание 1: Конвертер римских чисел в десятичные.
Задача 2: Написать функцию для преобразования римского числа в целое число.
"""


def roman_to_int(s: str) -> int:
    """
    Конвертирует римское число в десятичное.

    Args:
        s (str): Римское число (в формате строки).

    Returns:
        int: Десятичное число.
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    # Проходим по символам справа налево
    for char in reversed(s):
        current_value = roman_values[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value

    return result


# Примеры
if __name__ == "__main__":
    print("III ->", roman_to_int("III"))  # 3
    print("LVIII ->", roman_to_int("LVIII"))  # 58
    print("MCMXCIV ->", roman_to_int("MCMXCIV"))  # 1994