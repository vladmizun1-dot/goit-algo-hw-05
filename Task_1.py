def caching_fibonacci():
    cache = {} # Словник для збереження значень

    def fibonacci(n): # Функція для обчислення числа Фібоначчі
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache: # Перевірка, чи є значення в кеші
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Обчислення та збереження в кеші
        return cache[n]

    return fibonacci # Повертаємо функцію

# Тестування
if __name__ == "__main__":
    fib = caching_fibonacci()  # Перевірка значень
    print(f"fib(10) = {fib(10)}")  # Очікується 55
    print(f"fib(15) = {fib(15)}")  # Очікується 610
    print(f"fib(20) = {fib(20)}")  # Очікується 6765