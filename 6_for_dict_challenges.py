# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def find_duplicates(list_of_students):
    num_duplicate = {}
    for student in list_of_students:
        name = student['first_name']
        if name not in num_duplicate:
            num_duplicate[name] = 1
        else:
            num_duplicate[name] += 1
    # key - name, value - number
    return num_duplicate


for person, duplicate in find_duplicates(students).items():
    print(f'{person}: {duplicate}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def find_most_popular_name(person_dict):
    duplicates_sort_list = sorted(
        duplicates_dict.items(),
        key=lambda v: v[1],
        reverse=True
    )
    popular_name_f = duplicates_sort_list[0][0]
    num_popular_f = duplicates_sort_list[0][1]
    return popular_name_f, num_popular_f


duplicates_dict = find_duplicates(students)
popular_name, num_popular = find_most_popular_name(duplicates_dict)
print(f'Most popular name - {popular_name}, number of found {num_popular}')

# Задание 3
# Есть список учеников в нескольких классах, нужно
# вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
        {'first_name': 'Оля'}
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'}
    ]
]
for num_class, class_students in enumerate(school_students):
    duplicates_dict = find_duplicates(class_students)
    popular_name, a = find_mp_name(duplicates_dict)
    print(f'Most popular name in class {num_class}: {popular_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'},
                  {'first_name': 'Оля'},
                  {'first_name': 'Миша'}]},
    {'class': '3c',
     'students': [{'first_name': 'Олег'},
                  {'first_name': 'Миша'},
                  {'first_name': 'Макс'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def count_male_female(all_class):
    num_male_and_female = []
    for num_class in all_class:
        names = num_class['students']
        male_female_in_class = {
            'class': num_class['class'],
            'male': 0,
            'female': 0
        }
        for name_dict in names:
            name = name_dict['first_name']
            try:
                student = is_male[name]
                if student:
                    male_female_in_class['male'] += 1
                else:
                    male_female_in_class['female'] += 1
            except KeyError:
                print(f'There is no {name} in dictionare is_male')
        num_male_and_female.append(male_female_in_class)
    return num_male_and_female


result = count_male_female(school)
for each_class in result:
    result_class = each_class['class']
    most_female_in_class = each_class['female']
    most_male_in_class = each_class['male']
    print(f"In class {result_class} {most_female_in_class} female and"
          f" {most_male_in_class} male")

# Задание 5
# По информации о учениках разных классов нужно найти класс,
# в котором больше всего девочек и больше всего мальчиков.
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'},
                  {'first_name': 'Оля'},
                  {'first_name': 'Оля'},
                  {'first_name': 'Макс'}]},
    {'class': '3c',
     'students': [{'first_name': 'Олег'},
                  {'first_name': 'Миша'},
                  {'first_name': 'Маша'}]},
    {'class': '4b',
     'students': [{'first_name': 'Олег'},
                  {'first_name': 'Олег'},
                  {'first_name': 'Олег'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
result = count_male_female(school)
sorted_by_male = sorted(result, key=lambda m: m['male'], reverse=True)
sorted_by_female = sorted(result, key=lambda f: f['female'], reverse=True)

p_male_class = sorted_by_male[0]['class']
p_male_num = sorted_by_male[0]['male']
p_female_class = sorted_by_female[0]['class']
p_female_num = sorted_by_female[0]['female']

print(f"Most boys in class {p_male_class} - {p_male_num} boys")
print(f"Most girls in class {p_female_class} - {p_female_num} girls")
