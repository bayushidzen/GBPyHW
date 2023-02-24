# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам
a = 'а'
arr_count = []
texts = ['пара-ра-рам-кар', 'рам-пам-папам', 'па-ра-па-дам']
for i in range(len(texts)):
    print(texts[i])
    count = 0
    for j in range(len(texts[i])):
        if a in texts[i][j]:
            count +=1
    arr_count.append(count)
rhytm = False
max = arr_count[0]
for i in range(1, len(arr_count)):
    if max != arr_count[i]:
        rhytm = False
    else:
        rhytm = True
if rhytm: print('Парам пам-пам')
else: print('Пам парам')
