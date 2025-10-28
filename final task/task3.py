"""
Задание 1: Проверка монотонности массива.
Задача 3: Определить, является ли массив монотонно возрастающим или убывающим.
"""


def is_monotonic(nums):
    """
    Проверяет, является ли массив монотонным (возрастающим или убывающим).

    Args:
        nums (list): Список чисел.

    Returns:
        bool: True, если массив монотонный, иначе False.
    """
    if len(nums) <= 2:
        return True

    # Проверяем неубывающую последовательность
    non_decreasing = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

    # Проверяем невозрастающую последовательность
    non_increasing = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

    return non_decreasing or non_increasing


# Примеры
if __name__ == "__main__":
    print("Input: [1,2,2,3] ->", is_monotonic([1, 2, 2, 3]))  # True
    print("Input: [6,5,4,4] ->", is_monotonic([6, 5, 4, 4]))  # True
    print("Input: [1,3,2] ->", is_monotonic([1, 3, 2]))  # False