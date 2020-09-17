"""
Домашнее задание №2
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
# imports (std)
import os
import csv

# vaiables
current_dir = os.path.dirname(__file__)
dict_for_csv = [
    {'name': 'Max', 'age': 29, 'job': 'Enjineer'},
    {'name': 'Alex', 'age': 27, 'job': 'Trener'},
    {'name': 'Kira', 'age': 2, 'job': 'Best child ever'}
]


def main():
    with open(f'{current_dir}/family.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(dict_for_csv[0].keys())
        for item in dict_for_csv:
            csv_writer.writerow(item.values())


if __name__ == "__main__":
    main()
