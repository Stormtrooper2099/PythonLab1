# -*- coding: cp1251 -*-

import re

def password():
    print ('������� ������')
    print ('������ ������ ��������� �� 6 �� 12 ��������')

    while True:
        password = raw_input('������: ... ')
        if 6 <= len(password):
            break
        print ('������ ������ ��������� �� 6 �� 12 ��������')

    password_scores = {0:'�������', 1:'������', 2:'�������', 3:'�������'}
    password_strength = dict.fromkeys(['������� �������', '������ �������', '�����'], False)
    if re.search(r'[A-Z]', password):
        password_strength['������� �������'] = True
    if re.search(r'[a-z]', password):
        password_strength['������ �������'] = True
    if re.search(r'[0-9]', password):
        password_strength['�����'] = True

    score = len([x for x in password_strength.values() if x])

    print ('������ %s' % password_scores[score])

password()