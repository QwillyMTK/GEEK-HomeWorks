
from colorama import Fore, Style

# --- Часть 1: демонстрация внешней зависимости ---
print(Fore.RED + "Привет, мир! Это красный текст.")
print(Fore.GREEN + "А это зелёный текст.")
print(Style.RESET_ALL + "Сброс цвета обратно к стандартному.")

# --- Часть 2: алгоритм Two Sum ---
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Индексы:", [i, j])  # результат: [0, 1]
            print("Числа:", nums[i], "+", nums[j], "=", target)
