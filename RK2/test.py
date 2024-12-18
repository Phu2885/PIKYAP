import unittest
from main import StudentGroup, Course, task1, task2, task3


class TestCourseTasks(unittest.TestCase):

    def setUp(self):
        self.groups = [
            StudentGroup(1, 'Группа по экономике'),
            StudentGroup(2, 'Группа по искусственному интеллекту'),
        ]

        self.courses = [
            Course(1, 'Курс Основы экономики', 85, 1),
            Course(2, 'Машинное обучение', 90, 2),
            Course(3, 'Курс Финансовый менеджмент', 87, 1),
        ]

    def test_task1(self):
        expected = [
            ('Курс Основы экономики', 'Группа по экономике'),
            ('Курс Финансовый менеджмент', 'Группа по экономике'),
            ('Машинное обучение', 'Группа по искусственному интеллекту'),
        ]
        result = task1(self.groups, self.courses)
        self.assertEqual(result, expected)

    def test_task2(self):
        expected = [
            ('Машинное обучение', 90.0),
            ('Курс Финансовый менеджмент', 87.0),
            ('Курс Основы экономики', 85.0),
        ]
        result = task2(self.groups, self.courses)
        self.assertEqual(result, expected)

    def test_task3(self):
        expected = [
            ('Курс Основы экономики', ['Группа по экономике']),
            ('Курс Финансовый менеджмент', ['Группа по экономике']),
        ]
        result = task3(self.groups, self.courses, keyword="Курс")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
