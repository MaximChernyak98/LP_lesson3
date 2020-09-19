"""
Домашнее задание №2
Работа с файлами
1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
# imports (std)
import os, time

# vaiables
current_dir = os.path.abspath(os.getcwd())
file_to_search = 'referat.txt'


def main():
    try:
        path_to_referat = os.path.join(current_dir, 'referat.txt')
        with open(path_to_referat, 'r', encoding='utf-8') as referat:
            text = referat.read()
            # counting the number of characters
            length = len(text)
            print(length)
            # counting the number of words
            num_words = len(text.split())
            print(num_words)
            # replace points to exclamation point
            text_with_exc = text.replace('.', '!')
            # save changes in new file
            path_to_new_referat = os.path.join(current_dir, 'referat2.txt')
            with open(path_to_new_referat, 'w', encoding='utf-8') as referat2:
                referat2.write(text_with_exc)
    except FileNotFoundError:
        print(f'File not found {file_to_search}, checkout file existense')


if __name__ == "__main__":
    main()
