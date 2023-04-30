#создай приложение для запоминания информации


#отображение окна приложения 


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication,QGroupBox, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2  
        self.wrong3 = wrong3

app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(600, 400)

text = QLabel('Како национальности не сущестует?')
vop = QPushButton('Ответить')
t1 = QRadioButton('Энцы')
t2 = QRadioButton('Чулымцы')
t3 = QRadioButton('Смурфы')
t4 = QRadioButton('Алеуты')

answer = [t1, t2, t3, t4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(t1)
RadioGroup.addButton(t2)
RadioGroup.addButton(t3)
RadioGroup.addButton(t4)



RadioGroupBox = QGroupBox('Варианты ответов')


hl1 = QHBoxLayout()
vl1 = QVBoxLayout()
vl2 = QVBoxLayout()

vl1.addWidget(t1)
vl1.addWidget(t2)
vl2.addWidget(t3)
vl2.addWidget(t4)

hl1.addLayout(vl1)
hl1.addLayout(vl2)

RadioGroupBox.setLayout(hl1)

RadioGroupBox.hide()

AnsGroupBox = QGroupBox('Результат теста')
correct = QLabel('Правильно/Неправильно')
r_answer = QLabel('Правильный ответ')

vl3 = QVBoxLayout()
vl3.addWidget(correct)
vl3.addWidget(r_answer, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(vl3)


h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()

h1.addWidget(text, alignment = Qt.AlignCenter)
h2.addWidget(RadioGroupBox)
h2.addWidget(AnsGroupBox)
h3.addWidget(vop, alignment = Qt.AlignCenter)


v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)

win.setLayout(v1)

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    vop.setText('Ответить')
    RadioGroup.setExclusive(False)
    t1.setChecked(False)
    t2.setChecked(False)
    t3.setChecked(False)
    t4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_resoults():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    vop.setText('Следующий вопрос')

def click_OK():
    if vop.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    RadioGroupBox.show()
    show_question()

def show_correct(res):
    correct.setText(res)
    show_resoults()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        win.scor += 1
    else:
        if answer[1].isChecked or answer[2].isChecked or answer[3].isChecked():
            show_correct('Неверно!')
    print('Статистика')
    print('Количество вопросов = ', win.total)
    print('Правильных ответов = ', win.scor)
    print('Рейтинг:', round(win.scor / win.total * 100,1), '%')


def next_question():
    win.total += 1
    cur_question = randint(0,len(Question_list)-1)
    q = Question_list[cur_question]
    ask(q)
    print('Статистика')
    print('Количество вопросов = ', win.total)
    print('Правильных ответов = ', win.scor)




Question_list = []



 
p = Question('Сколько языков в мире ', '7151 ', '3', '32', '4566')
w = Question('Глубина озера Байкал', '1642', '6988', '1344', '45')









Question_list.append(Question('Государственый язык в Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
Question_list.append(p)
Question_list.append(w)
Question_list.append(Question('Столица Китая', 'Пекин', 'Токио', 'Шан-Хай', 'Буэнос Айрос'))
Question_list.append(Question('Какого цвета нет во флаге РФ', 'зеленый', 'красный','белый', 'синий'))
Question_list.append(Question('Сколько дней шла Ленинградская битва', '200', '145','235','193'))
Question_list.append(Question('Первый челоек ступивший на луну', 'Армстронг', 'Гагарин','Терешкова','Королёв'))
Question_list.append(Question('Первый Царь Руси', 'Рюрик', 'Иван Грозный', 'Сталин', 'Хрущев'))
Question_list.append(Question('Какой памятник стоит на Мамаевом Кургане', 'Родина мать зовет', 'статуя Свободы', 'Царь пушка', 'Голова Ленина'))
Question_list.append(Question('Как зовут Героя Советского Союза: связист соединивший кабель зубами', 'Матвей Путилов', 'Яков Павлов', 'Рокоссовский', 'Тимушенко'))
Question_list.append(Question('Назовите столицу Казахстана: ','Астана','Актау','Алмата','Актобе'))

win.total = 0
win.scor = 0

next_question()

vop.clicked.connect(click_OK)




win.show()
app.exec_()








