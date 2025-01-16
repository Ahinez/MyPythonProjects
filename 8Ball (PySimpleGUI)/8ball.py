import PySimpleGUI as sg
from random import *

sg.theme('Black')

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений	', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', \
           'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', \
            'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']



layout = [[sg.Text('Задавай интерисующий тебя вопрос.', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=True, key='-QUEST-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('8 ball chat', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

while True:     # The Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break

    if event == 'SEND':
        question = values['-QUEST-'].rstrip()
        print(f'Вопрос: {question}', flush=True)
        print(f'Ответ шара: {choice(answers)}')

window.close()