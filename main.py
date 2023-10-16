                            #1 николай
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True

#2 season_events

months = {
        1: 'Январе',
        2: 'Феврале',
        3: 'Марте',
        4: 'Апреле',
        5: 'Мае',
        6: 'Июне',
        7: 'Июле',
        8: 'Августе',
        9: 'Сентябре',
        10: 'Октябре',
        11: 'Ноябре',
        12: 'Декабре'
    }


def season_events(number_of_month):
   if not isinstance(number_of_month, int) and 1 <= number_of_month <= 12:
        print('Требуется ввести реальный номер месяца')
	        return
   if number_of_month in range(3, 6):
    print(f'Вы родились в {months[number_of_month]}. Птицы пели прекрасные песни')
   elif number_of_month in range(6, 9):
           print(f'Вы родились в {months[number_of_month]}. Солнце светило ярче чем когда-либо')
   elif number_of_month in range(9, 12):
     print(f'Вы родились в {months[number_of_month]}. Урожай был невероятным')
   else:
        print(f'Вы родились в {months[number_of_month]}. За окном падал белый снег')

#3 пароль

import string


def check_pass(pwd):

    err = {
    'length': 'Длина пароля не равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
    'digits': 'Нет цифр в пароле',
    'spec': 'Отсутствуют спецсимволы в пароле',
    'bad_symbols': 'В пароле использованы непредусмотренные символы'
    }

    if len(pwd) == 8:
        err.pop('length')

    if pwd.lower() != pwd:
        err.pop('upper')

    if pwd.upper() != pwd:
        err.pop('lower')

    if any(map(str.isdigit, pwd)):
        err.pop('digits')

    if ('*' in pwd) or ('-' in pwd) or ('#' in pwd):
        err.pop('spec')

    allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

    if (set(pwd) - set(allowed_sym)) == set():
        err.pop('bad_symbols')

    if len(err) == 0:
        print('Пароль идеален')
    else:
        print(*err.values(), sep='; ')


check_pass('FIUwnf')

#4

def is_divisible_by_6(number):
    lst_str_digits = list(str(abs(number)))
    lst_digits = list(map(int, lst_str_digits))
    sum_digits = sum(lst_digits)
    if (sum_digits % 3 == 0) and (lst_digits[-1] % 2 == 0):
        return f'Число {number} делится на 6'
    else:
        return f'Число {number} неделимо на 6'

#5

def search_substr(subst, st):
    if subst.lower() in st.lower():
        	return 'Есть контакт!'
    else:
    	return 'Мимо!'

print(search_substr('ппфы', 'кцп32й'))

#6 индексы

def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last

print(first_last('a', 'fgws'))

#7

from collections import Counter


def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

print(top3('kkwwkkwwrr'))

#8

def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st


# Тесты
print(camel('llslslslsl'))

#9

def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

print(shortener('1(2)3(4)5(6)'))

#10

def more_than_five(lst):
    new_lst = []
    for number in lst:
        if abs(number) > 5:
            new_lst.append(number)
    return new_lst

print(more_than_five([11,3,-33,524,-1,-444,2]))

#11

letters = 'ЫдУоЦАЙжАЙдАь'
clean_string = ''
for letter in letters:
    if not letter.isupper():
        clean_string += letter
letters = clean_string
print(letters)

#12

#13

#14

def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

print(sum_range(2, 12))


#15


def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

three_args(var1=21)

#16

import inspect
import math


def inspect_function(some_func):
    print(f'Анализируем функцию {some_func.__name__}')
    for param in inspect.signature(some_func).parameters.values():
        print(param.name, param.kind, sep=': ')


def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass

inspect_function(my_func)

#17 Антон

from datetime import datetime
from time import sleep


def time_now(msg, *, dt=None):
    dt = dt or datetime.now()
    print(msg, dt)

time_now('Время: ')
