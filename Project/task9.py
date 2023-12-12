#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {}

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        # Добавить класс
        elif command == 'add':
            school_class = input('Класс: ').upper()
            students = int(input('Количество учеников: '))
            school.setdefault(school_class, students)

        # изменить количество учеников в классе
        elif command == 'edit':
            school_class = input('Изменить класс: ').upper()
            school[school_class] = int(input('Количество учеников: '))

        # Удалить класс
        elif command == 'delete':
            school_class = input('Удалить класс: ').upper()
            del school[school_class]

        # Вывести данные
        elif command == 'list':
            line = '+-{}-+-{}-+'.format('-' * 4, '-' * 10,)
            print(line)

            print('| {:^4} | {:^10} |'.format("Класс", "Ученики"))
            print(line)

            for key, value in school.items():
                print('| {:>4} | {:<10} |'.format(key, value))
            print(line)

        # Вычислить общее количество учащихся в школе
        elif command == 'total':
            total_students = sum(school.values())
            print("Общее количество учащихся в школе:", total_students)

        # Вывести справку о работе с программой.
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить новый класс;")
            print("edit - изменить количество учащихся;")
            print("delete - удалить класс;")
            print("total - вывести общее количество учащихся;")
            print("list - вывести список классов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

