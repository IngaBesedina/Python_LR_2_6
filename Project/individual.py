#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Создаем список из словарей
    students = []

    # Ввод данных с клавиатуры
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        surname = input("Введите фамилию и инициалы: ")
        group_num = input("Введите номер группы: ")
        print('Введите оценки: ')
        grades = [int(n) for n in input().split()]

        student = {
            'name': surname,
            'group_number': group_num,
            'grades': grades
        }
        students.append(student)

    # Сортировка по возрастанию среднего балла
    students.sort(key=lambda x: sum(x['grades']) / 5)

    # Вывод на экран фамилий и номеров групп для студентов с оценками 4 и 5
    found = False
    for student in students:
        if all(grade >= 4 for grade in student['grades']):
            print(f"Студент: {student['name']}, Группа: {student['group_number']}")
            found = True

    if not found:
        print("Студентов с оценками 4 и 5 нет")
