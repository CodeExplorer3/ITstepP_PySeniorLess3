import inspect

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
        self.pensione = value >= 60

    def info_person(self):
        return f'{self.name} {self.surname}, вік: {self.age}, пенсіонер: {"так" if self.pensione else "ні"}'


class Worker(Person):
    position: str
    salary: float
    hours_per_week: int

    def __init__(self, name: str, surname: str, age: int, position: str, salary: float, hours_per_week: int):
        super().__init__(name, surname, age)
        self.position = position
        self.salary = salary
        self.hours_per_week = hours_per_week

    def work(self):
        return f"{self.name} {self.surname} працює на позиції {self.position}."

    def salary_info(self):
        return f"Зарплата: {self.salary} за {self.hours_per_week} годин на тиждень."


class StudySubject:
    name: str
    hours: int
    level: str

    def __init__(self, name: str, hours: int, level: str):
        self.name = name
        self.hours = hours
        self.level = level

    def __str__(self):
        return f'{self.name} {self.level}, кількість годин {self.hours}'


class Student(Person):
    first_name: str
    second_name: str
    is_offline: bool
    study_subject: StudySubject

    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject, is_offline=True):
        # Инициализируем базовый класс
        super().__init__(first_name, second_name, age)
        self.first_name = first_name  # Сохраняем отдельно
        self.second_name = second_name  # Сохраняем отдельно
        self.is_offline = is_offline
        self.study_subject = study_subject

    def __str__(self):
        study_type = 'offline' if self.is_offline else 'online'
        student_info = f'{self.second_name} {self.first_name}, вік {self.age}, навчається {study_type}'
        return f'{student_info}\n{self.study_subject}'



def inspect_class(cls):
    """
    Выводит список атрибутов и методов для указанного класса.
    """
    attributes = [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]
    methods = [method[0] for method in inspect.getmembers(cls, predicate=inspect.isfunction)]

    print(f"Класс: {cls.__name__}")
    print("Атрибуты:")
    for attr in attributes:
        print(f"  - {attr}")
    print("Методы:")
    for method in methods:
        print(f"  - {method}")
    print("-" * 50)


# Примеры использования
print("Lesson 3: Work with several classes\n")

# Создаем объекты для теста
py_senior = StudySubject('Python', 18, 'Senior')
student = Student('Красюков', "Іван", 13, py_senior)
worker = Worker('Олександр', 'Іванов', 45, 'Програміст', 30000, 40)

# Интроспекция классов
inspect_class(Student)
inspect_class(Worker)

# Вывод данных о созданных объектах
print("Данные объектов:")
print(student)
print(worker.work())
print(worker.salary_info())
