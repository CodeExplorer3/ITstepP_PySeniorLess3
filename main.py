class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')
class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def convert_to_float(value: str):
        """
        Конвертирует строку в число с плавающей точкой.
        Если невозможно, возвращает None и выводит сообщение об ошибке.
        """
        try:
            result = float(value)
            return result
        except ValueError:
            print(f"Ошибка: '{value}' невозможно преобразовать в float.")
            return None
        finally:
            print(f"Попытка конвертации '{value}' завершена.")

    @staticmethod
    def add(a: float, b: float):
        return a + b

    @staticmethod
    def subtract(a: float, b: float):
        return a - b

    @staticmethod
    def multiply(a: float, b: float):
        return a * b

    @staticmethod
    def divide(a: float, b: float):
        """
        Делит первое число на второе.
        Если деление на ноль, возвращает None и выводит сообщение об ошибке.
        """
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Ошибка: деление на ноль невозможно.")
            return None
        finally:
            print(f"Попытка деления {a} на {b} завершена.")


# Пример использования
if __name__ == "__main__":
    calc = Calculator()

    # Пример конвертации
    number = calc.convert_to_float("123.45")
    print(f"Конвертированное число: {number}")

    invalid_number = calc.convert_to_float("abc")
    print(f"Конвертированное число: {invalid_number}")

    # Пример математических операций
    a, b = 10, 5
    print(f"Сложение: {calc.add(a, b)}")
    print(f"Вычитание: {calc.subtract(a, b)}")
    print(f"Умножение: {calc.multiply(a, b)}")
    print(f"Деление: {calc.divide(a, b)}")

    # Пример деления на ноль
    print(f"Деление на ноль: {calc.divide(a, 0)}")
