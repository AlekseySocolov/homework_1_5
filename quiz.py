def f_quiz():
    to_repeat = 'Да'
    correct_answers = 0
    number_of_questions = 5
    name = ['Николая Ивановича Лобачевского','Николая Ивановича Пирогова','Ивана Федоровича Крузенштерна','Михаила Илларионовича Кутузова','Наполеона I Бонапарта','Вольфганга Амадея Моцарта','Адама Смита','Иммануила Канта','Джорджа Вашингтона','Майера Амшеля Ротшильда']
    date_of_birth = ['01.12.1792','25.11.1810','19.11.1770','16.09.1745','15.08.1769','27.01.1756','05.06.1723','22.04.1724','22.02.1732','23.02.1744']
    birthday = ['первого декабря 1792','двадцатьпятого ноября 1810','девятнадцатого ноября 1770','шестнадцатого сентября 1745','пятнадцатого августа 1769','двадцатьседьмого января 1756','пятого июня 1723','двадцатьвторого апреля 1724','двадцатьвторого февраля 1732','двадцатьтретьего февраля 1744']
    import random
    numbers = [0,1,2,3,4,5,6,7,8,9]
    to_repeat = 'Да'
    while to_repeat == 'Да':
        result = random.sample(numbers, number_of_questions)
        for i in result:
            if input(f'Введите дату рождения {name[i]} в формате дд.мм.гггг : ') == date_of_birth[i]:
                correct_answers += 1
            else:
                print(f'Правильный ответ - {birthday[i]}')
        print('Количество верных ответов - ', correct_answers)
        print('Количество неверных ответов - ', 5-correct_answers)
        to_repeat = input('Хотите начать викторину с начала? Да/Нет :')