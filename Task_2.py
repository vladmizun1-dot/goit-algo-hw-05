from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]: # Аналізуємо текст і генеруємо числа
  
    for word in text.split(): # Розділяємо текст на слова пробілами
        try:
            if '.' in word or word.isdigit(): # Перевіряємо, чи є слово числом цілим чи з крапкою
                yield float(word)
        except ValueError: # якщо слово не число то пропускаємо його
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
  
    total = 0.0
    # Отримуємо числа з генератора по одному
    for number in func(text):
        total += number
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1234.01 як основний дохід, доповнений додатковими надходженнями 27.45 і = 85.5 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
