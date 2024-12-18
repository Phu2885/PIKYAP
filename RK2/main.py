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

def task1(groups, courses):
    """
    Возвращает список всех студентов и курсов, отсортированный по курсам.
    """
    one_to_many = [(course.title, group.name)
                   for group in groups
                   for course in courses
                   if course.group_id == group.id]
    return sorted(one_to_many, key=itemgetter(0))

def task2(groups, courses):
    """
    Возвращает список курсов с суммарной средней оценкой студентов.
    """
    course_avg_grades = {}

    for group in groups:
        group_courses = [course for course in courses if course.group_id == group.id]
        for course in group_courses:
            if course.title not in course_avg_grades:
                course_avg_grades[course.title] = []
            course_avg_grades[course.title].append(course.avg_grade)

    return sorted([(course, sum(grades) / len(grades))
                   for course, grades in course_avg_grades.items()], key=itemgetter(1), reverse=True)

def task3(groups, courses, keyword="Курс"):
    """
    Возвращает список курсов с указанным ключевым словом в названии и студентов на этих курсах.
    """
    result = []
    courses_with_keyword = [course for course in courses if keyword in course.title]

    for course in courses_with_keyword:
        students_in_course = [group.name for group in groups if group.id == course.group_id]
        result.append((course.title, students_in_course))

    return result

if __name__ == '__main__':
    groups = [
        StudentGroup(1, 'Группа по экономике'),
        StudentGroup(2, 'Группа по искусственному интеллекту'),
        StudentGroup(3, 'Группа по биотехнологиям'),
        StudentGroup(4, 'Группа по инженерии'),
        StudentGroup(5, 'Группа по медицине'),
        StudentGroup(6, 'Группа по химии'),
    ]

    courses = [
        Course(1, 'Курс Основы экономики', 85, 1),
        Course(2, 'Машинное обучение', 90, 2),
        Course(3, 'Биотехнологии и устойчивое развитие', 75, 3),
        Course(4, 'Механика материалов', 80, 4),
        Course(5, 'Курс Анатомия человека', 88, 5),
        Course(6, 'Органическая химия', 93, 6),
        Course(7, 'Финансовый менеджмент', 87, 1),
        Course(8, 'Нейронные сети', 76, 2),
        Course(9, 'Биохимия', 84, 3),
        Course(10, 'Системы управления проектами', 92, 4),
        Course(11, 'Фармакология', 89, 5),
        Course(12, 'Неорганическая химия', 78, 6),
    ]

    print('Задание 1')
    for course, group in task1(groups, courses):
        print(f"{course} - {group}")

    print('\nЗадание 2')
    for course, avg_grade in task2(groups, courses):
        print(f"{course} - {avg_grade:.2f}")

    print('\nЗадание 3')
    for course, students in task3(groups, courses):
        print(f"{course}: {', '.join(students)}")
