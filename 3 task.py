class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: Неверный лектор или курс.'

    def calculate_average_grade(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет"
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.2f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок от студентов

    def calculate_rating(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        avg_rating = self.calculate_rating()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_rating:.2f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_rating() < other.calculate_rating()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Пример использования классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']

# Эксперт оценивает студента
cool_reviewer.rate_student(best_student, 'Python', 8)

# Студент оценивает лектора
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

# Проверка вывода
print(best_student)
print(cool_lecturer)
print(cool_reviewer)

# Создание еще одного лектора для сравнения
another_lecturer = Lecturer('Anna', 'Russia')
another_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(another_lecturer, 'Python', 10)

# Проверка сравнения лекторов
print(f"Лектор {cool_lecturer.name} меньше лектора {another_lecturer.name}? {cool_lecturer < another_lecturer}")

# Создание еще одного студента для сравнения
another_student = Student('Oleg', 'Petrov', 'man')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Базы данных']
cool_reviewer.rate_student(another_student, 'Python', 9)
best_student.rate_lecturer(another_lecturer, 'Python', 8)

# Проверка сравнения студентов
print(f"Студент {best_student.name} меньше студента {another_student.name}? {best_student < another_student}")