# -*- coding: cp1251 -*-

import re

def password():
    print ('Введите пароль')
    print ('Пароль должен содержать от 6 до 12 символов')

    while True:
        password = raw_input('Пароль: ... ')
        if 6 <= len(password):
            break
        print ('Пароль должен содержать от 6 до 12 символов')

    password_scores = {0:'Ужасный', 1:'Слабый', 2:'Средний', 3:'Надёжный'}
    password_strength = dict.fromkeys(['Высокий регистр', 'Нижний регистр', 'Цифры'], False)
    if re.search(r'[A-Z]', password):
        password_strength['Высокий регистр'] = True
    if re.search(r'[a-z]', password):
        password_strength['Нижний регистр'] = True
    if re.search(r'[0-9]', password):
        password_strength['Цифры'] = True

    score = len([x for x in password_strength.values() if x])

    print ('Пароль %s' % password_scores[score])

password()