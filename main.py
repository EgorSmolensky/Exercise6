class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average(self):
        total, count = 0, 0
        for course in self.grades:
            total += sum(self.grades[course])
            count += len(self.grades[course])
        return total / count

    def __str__(self):
        average = round(self._average(), 2)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self._average() < other._average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average(self):
        total, count = 0, 0
        for course in self.grades:
            total += sum(self.grades[course])
            count += len(self.grades[course])
        return total / count

    def __str__(self):
        average = round(self._average(), 2)
        return super().__str__() + f'\nСредняя оценка за лекции: {average}'

    def __lt__(self, other):
        return self._average() < other._average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_hwgrade_per_course(students, course):
    total, count = 0, 0
    for student in students:
        if course in student.courses_in_progress:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 2)


def average_lecturegrade_per_course(lecturers, course):
    total, count = 0, 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 2)


student1 = Student('Егор', 'Смоленский', 'male')
student1.courses_in_progress += ['Матанализ для тех, кто шарит', 'Дифференциальная геометрия', 'Ракетодинамика']
student1.finished_courses += ['Физика космоса']
student2 = Student('Кристина', 'Надина', 'female')
student2.courses_in_progress += ['Теория квазимножеств', 'Аэронавтика']
student2.finished_courses += ['Матанализ для тех, кто шарит']

lecturer1 = Lecturer('Григорий', 'Перельман')
lecturer1.courses_attached += ['Матанализ для тех, кто шарит', 'Теория квазимножеств', 'Дифференциальная геометрия']
lecturer2 = Lecturer('Константин', 'Циолковский')
lecturer2.courses_attached += ['Физика космоса', 'Аэронавтика', 'Ракетодинамика']

reviewer1 = Reviewer('Анатолий', 'Мальцев')
reviewer1.courses_attached += ['Матанализ для тех, кто шарит', 'Теория квазимножеств', 'Дифференциальная геометрия']
reviewer2 = Reviewer('Сергей', 'Королев')
reviewer2.courses_attached += ['Физика космоса', 'Аэронавтика', 'Ракетодинамика']

reviewer1.rate_hw(student1, 'Матанализ для тех, кто шарит', 10)
reviewer1.rate_hw(student1, 'Матанализ для тех, кто шарит', 9)
reviewer1.rate_hw(student1, 'Матанализ для тех, кто шарит', 10)
reviewer1.rate_hw(student1, 'Дифференциальная геометрия', 9)
reviewer1.rate_hw(student1, 'Дифференциальная геометрия', 9)
reviewer1.rate_hw(student2, 'Теория квазимножеств', 8)
reviewer1.rate_hw(student2, 'Теория квазимножеств', 9)
reviewer1.rate_hw(student2, 'Теория квазимножеств', 8)

reviewer2.rate_hw(student1, 'Ракетодинамика', 9)
reviewer2.rate_hw(student1, 'Ракетодинамика', 9)
reviewer2.rate_hw(student1, 'Ракетодинамика', 9)
reviewer2.rate_hw(student2, 'Аэронавтика', 10)

print('Проверяющие преподаватели:')
print(reviewer1)
print(reviewer2)
print()

print('Студенты:')
print(student1)
print(student2)
print(student1 < student2)
print()

student1.rate_lecture(lecturer1, 'Матанализ для тех, кто шарит', 8)
student1.rate_lecture(lecturer1, 'Матанализ для тех, кто шарит', 7)
student1.rate_lecture(lecturer1, 'Матанализ для тех, кто шарит', 8)
student1.rate_lecture(lecturer1, 'Дифференциальная геометрия', 10)
student1.rate_lecture(lecturer1, 'Дифференциальная геометрия', 10)
student1.rate_lecture(lecturer2, 'Ракетодинамика', 10)
student1.rate_lecture(lecturer2, 'Ракетодинамика', 9)
student1.rate_lecture(lecturer2, 'Ракетодинамика', 10)

student2.rate_lecture(lecturer1, 'Теория квазимножеств', 8)
student2.rate_lecture(lecturer1, 'Теория квазимножеств', 7)
student2.rate_lecture(lecturer1, 'Теория квазимножеств', 7)
student2.rate_lecture(lecturer2, 'Аэронавтика', 10)

print('Лекторы:')
print(lecturer1)
print(lecturer2)
print(lecturer1 < lecturer2)
print()

print('Средняя оценка за домашнюю работу:')
print(average_hwgrade_per_course([student1, student2], 'Матанализ для тех, кто шарит'))
print('Средняя оценка лекций:')
print(average_lecturegrade_per_course([lecturer1, lecturer2], 'Матанализ для тех, кто шарит'))