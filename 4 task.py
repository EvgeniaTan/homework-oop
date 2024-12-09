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
        self.grades = {}

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

# Функции для подсчета средней оценки
def average_grade_students(students, course):
    total_grade = 0
    total_students = 0

    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            total_students += len(student.grades[course])
    
    return total_grade / total_students if total_students > 0 else 0

def average_grade_lecturers(lecturers, course):
    total_rating = 0
    total_lecturers = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            total_rating += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])

    return total_rating / total_lecturers if total_lecturers > 0 else 0

# Пример использования классов
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']

another_student = Student('Oleg', 'Petrov', 'male')
another_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Anna', 'Russia')
another_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']

# Эксперт оценивает студентов
cool_reviewer.rate_student(best_student, 'Python', 8)
cool_reviewer.rate_student(another_student, 'Python', 9)

# Студенты оценивают лекторов
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
another_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(another_lecturer, 'Python', 10)

# Проверка вывода
print(best_student)
print(another_student)
print(cool_lecturer)
print(another_lecturer)
print(cool_reviewer)

# Проверка среднего значения оценок студентов и лекторов
print(f'Средняя оценка студентов по курсу Python: {average_grade_students([best_student, another_student], "Python"): .2f}')
print(f'Средняя оценка лекторов по курсу Python: {average_grade_lecturers([cool_lecturer, another_lecturer], "Python"): .2f}')

# Проверка сравнения лекторов
print(f"Лектор {cool_lecturer.name} меньше лектора {another_lecturer.name}? {cool_lecturer < another_lecturer}")

# Проверка сравнения студентов
print(f"Студент {best_student.name} меньше студента {another_student.name}? {best_student < another_student}")