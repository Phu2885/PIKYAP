from operator import itemgetter

class StudentGroup:
    """Студенческая группа"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Course:
    """Учебный курс"""

    def __init__(self, id, title, avg_grade, group_id):
        self.id = id
        self.title = title
        self.avg_grade = avg_grade
        self.group_id = group_id


class GroupCourse:
    """
    'Группы на курсе' для реализации 
    связи многие-ко-многим
    """

    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id


# Студенческие группы
groups = [
    StudentGroup(1, 'Группа по экономике'),
    StudentGroup(2, 'Группа по искусственному интеллекту'),
    StudentGroup(3, 'Группа по биотехнологиям'),
    StudentGroup(4, 'Группа по инженерии'),
    StudentGroup(5, 'Группа по медицине'),
    StudentGroup(6, 'Группа по химии'),
]
# Учебные курсы
courses = [
    Course(1, 'Основы экономики', 85, 1),
    Course(2, 'Машинное обучение', 90, 2),
    Course(3, 'Биотехнологии и устойчивое развитие', 75, 3),
    Course(4, 'Механика материалов', 80, 4),
    Course(5, 'Анатомия человека', 88, 5),
    Course(6, 'Органическая химия', 93, 6),
    Course(7, 'Финансовый менеджмент', 87, 1),
    Course(8, 'Нейронные сети', 76, 2),
    Course(9, 'Биохимия', 84, 3),
    Course(10, 'Системы управления проектами', 92, 4),
    Course(11, 'Фармакология', 89, 5),
    Course(12, 'Неорганическая химия', 78, 6),
]

# Связи многие-ко-многим
groups_courses = [
    GroupCourse(1, 1),
    GroupCourse(2, 2),
    GroupCourse(3, 3),
    GroupCourse(4, 4),
    GroupCourse(5, 5),
    GroupCourse(6, 6),
    GroupCourse(1, 7),
    GroupCourse(2, 8),
    GroupCourse(3, 9),
    GroupCourse(4, 10),
    GroupCourse(5, 11),
    GroupCourse(6, 12),
]

def main():
    """Основная функция"""

    # Запрос 1: Список всех студентов и курсов, отсортированный по курсам
    print('Задание А1')
    # Соединяем курсы и группы
    one_to_many = [(course.title, group.name)
                   for group in groups
                   for course in courses
                   if course.group_id == group.id]
    
    # Сортируем по названию курса
    sorted_one_to_many = sorted(one_to_many, key=itemgetter(0))
    
    for course, group in sorted_one_to_many:
        print(f"{course} - {group}")

    # Запрос 2: Список курсов с суммарной средней оценкой студентов
    print('\nЗадание А2')
    course_avg_grades = {}
    
    for group in groups:
        group_courses = [course for course in courses if course.group_id == group.id]
        for course in group_courses:
            if course.title not in course_avg_grades:
                course_avg_grades[course.title] = []
            course_avg_grades[course.title].append(course.avg_grade)
    
    # Суммируем и считаем среднюю оценку для каждого курса
    avg_grades_sorted = sorted([(course, sum(grades)/len(grades)) 
                                for course, grades in course_avg_grades.items()], key=itemgetter(1), reverse=True)
    
    for course, avg_grade in avg_grades_sorted:
        print(f"{course} - {avg_grade:.2f}")

    # Запрос 3: Список курсов с "Курс" в названии и студентов на этих курсах
    print('\nЗадание А3')
    courses_with_kurs = [course for course in courses if 'Курс' in course.title]
    
    for course in courses_with_kurs:
        students_in_course = [group.name for group in groups if group.id == course.group_id]
        print(f"{course.title}: {', '.join(students_in_course)}")

if __name__ == '__main__':
    main()
