'''
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
'''
# imports (std)
import datetime as date
import locale

# config
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')

# variables
date_to_parse = '2001/01/25 12:10:03.234567'


def print_date(in_date):
    # print now, yesterday and month_ago
    now = date.datetime.now()
    yesterday = now - date.timedelta(days=1)
    month_ago = now - date.timedelta(days=30)
    print(now)
    print(yesterday)
    print(month_ago)
    # parse entered string to format
    if type(in_date) == str:
        try:
            print(date.datetime.strptime(in_date, '%y/%m/%d %H:%M:%S.%f'))
        except ValueError:
            print('Entered string does not match format YY/MM/DD HH:MM:SS.uS')
    else:
        print('The entered data is not a string')


if __name__ == "__main__":
    print_date(date_to_parse)
