# Задача 1 с сайта
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_num = int(input('Введите номер дня недели: '))
match day_num:
    case "1":
        print('Увы, сегодня не выходной')
    case "2":
        print('Увы, сегодня не выходной')
    case "3":
        print('Увы, сегодня не выходной')
    case "4":
        print('Увы, сегодня не выходной')
    case "5":
        print('Увы, сегодня не выходной')
    case "6":
        print('Ура! Суббота! Отдыхаем!')
    case "7":
        print('О! Уже воскресенье! А была ли суббота?')
    case "0":
        print('А я смотрю вы отсчет дней начинаете как настоящий программист)')
    case _:
        print('Добро пожаловать на Землю! Из какой вы вселенной?')