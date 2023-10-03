import math

class Calculator:
    def __init__(self):
        pass

    def calculate_sum(self, numbers):
        return sum(numbers)

    def calculate_subtraction(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def calculate_multiplication(self, numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def calculate_division(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result

    # Добавьте другие операции по аналогии


calculator = Calculator()

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == "0":
        break

    try:
        numbers = []
        while True:
            number = input("Введите число (или 'Результат' для завершения ввода): ")
            if number == "Результат":
                break
            numbers.append(float(number))

        if choice == "1":
            result = calculator.calculate_sum(numbers)
            print("Результат сложения:", result)
        elif choice == "2":
            result = calculator.calculate_subtraction(numbers)
            print("Результат вычитания:", result)
        elif choice == "3":
            result = calculator.calculate_multiplication(numbers)
            print("Результат умножения:", result)
        elif choice == "4":
            result = calculator.calculate_division(numbers)
            print("Результат деления:", result)
        # Добавьте другие операции по аналогии
        else:
            print("Неверный выбор операции")
    except ValueError:
        print("Некорректный ввод чисел")

    print()