#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    N = 5
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        if command == "add":
            name = input("Фамилия и инициалы: ")
            num = int(input("Номер группы: "))
            grade = [int(n) for n in input().split()]

            student = {
                'name': name,
                'num': num,
                'grades': grade,
            }

            students.append(student)
            sorted_students = sorted(students, key=lambda x: sum(x['grades']) / len(x['grades']))

        elif command == 'list':
            line = '+-{}-+-{}-+'.format('-' * 20, '-' * 14)
            print(line)
            print(
                '| {:^20} | {:^14} |'.format("Ф.И.О", "Номер группы"))
            print(line)

            count = 0.
            for student in sorted_students:
                if 4 in student['grades'] or 5 in student['grades']:
                    print('| {:^20} | {:^14} |'.format(student.get('name', ''), student.get('num', '')))
                    count += 1

            if count == 0:
                print('Нет студентов, имеющих оценки 4 или 5 ')
            print(line)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
