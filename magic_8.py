# Магический шар 8
from random import randint

answer_list = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова',	'Даже не думай',
'Предрешено',	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет',
'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать',	'По моим данным - нет',
'Определённо да',	'Знаки говорят - да',	'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом',	'Да',	'Сконцентрируйся и спроси опять',	'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print('Привет', name)
def choice():
    print('Задай свой вопрос')
    question = input()
    rnd = randint(1,21)
    return print(answer_list[rnd - 1])

choice()
while True:
    ans = input('Остались ли у вас вопросы?(да/нет) ')
    if ans.lower() in ('д', 'да', 'yes', 'y'):
        choice()
        continue
    else:
        break

print('Возвращайся если возникнут вопросы!')