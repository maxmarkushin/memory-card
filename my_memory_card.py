#подключаем библиотеки
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
from random import *





#создаем окно
app = QApplication([])
window = QWidget()
window.resize(600,400)
window.setWindowTitle("Конкурс от навального")


class Question():
    def __init__(self,question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question=question
        self.right_answer=right_answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
questions = []
questions.append(Question("Скока стоиt дворец питина","100 млрд рубасов","100 млрд dollars","50 млрд рубасов","100 млн рубасов"))
questions.append(Question("Скока времени Леха был в коме","2 недели и три дня","месяц","год","не был в коме"))
questions.append(Question("Сколько лет дали лехе","2 года 8 месяцев","5 лет","пожизненно","не дали срока"))
questions.append(Question("Сколько лет питин уже у власти","20 лет","всю жизнь","год","2 срока презедентских"))
questions.append(Question("Когда была уничтожена западная римская империя","476 г нашей эры","никогда","476 г до нашей эры","она в ссср"))

question = QLabel("Скока стоиt дворец питина")
#саздаем группу атвитав 
RGB = QGroupBox("Варианты атвita")
btn_answer1 = QRadioButton("100 млн рубасов")
btn_answer2 = QRadioButton("50 млрд рубасов")
btn_answer3 = QRadioButton("100 млрд рубасов")
btn_answer4 = QRadioButton("100 млрд dollars")
radiogroup = QButtonGroup()
radiogroup.addButton(btn_answer1)
radiogroup.addButton(btn_answer2)
radiogroup.addButton(btn_answer3)
radiogroup.addButton(btn_answer4)


#создаем результат

ans_RGB = QGroupBox("RESULT")
result = QLabel("Прав ты ,или нет")
correct = QLabel("Ответ будет тут :")


layuot_right = QVBoxLayout()

layuot_right.addWidget(result, alignment = Qt.AlignTop)
layuot_right.addWidget(correct, alignment = Qt.AlignCenter)

ans_RGB.setLayout(layuot_right)
ans_RGB.hide()
#кнопочки
layuot_main = QVBoxLayout()
layuot_main1 = QVBoxLayout()
layuot_main2 = QHBoxLayout()
layuot_main.addWidget(question, alignment = Qt.AlignCenter)
layuot_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layuot_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layuot_main1.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layuot_main1.addWidget(btn_answer4, alignment = Qt.AlignCenter)
#размещаем виджеты на линиях
layuot_main2.addLayout(layuot_main)
layuot_main2.addLayout(layuot_main1)
RGB.setLayout(layuot_main2)
button2 = QPushButton("pasadit")
layuot_main3 = QHBoxLayout()
layuot_main3.addWidget(button2,alignment = Qt.AlignCenter)
general_line = QVBoxLayout()
general_line.addWidget(question,alignment = Qt.AlignHCenter)
general_line.addWidget(RGB,alignment = Qt.AlignHCenter)
general_line.addWidget(ans_RGB,alignment = Qt.AlignCenter)
general_line.addLayout(layuot_main3)
window.setLayout(general_line)
window.show()

def show_result():
    RGB.hide()
    ans_RGB.show()
    button2.setText("поновой")
    

def show_question():
    RGB.show()
    ans_RGB.hide()
    button2.setText("гожить")
    radiogroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    radiogroup.setExclusive(True)

answers = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)
    question.setText(q.question)
    correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Праilьна")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("incorrect")


def next_question():
    cur_question=randint(0,len(questions)-1)
    a = questions[cur_question]
    ask(a)

def click_ok():
    if button2.text()=="гожить":
        check_answer()
    else: 
        next_question()

button2.clicked.connect(click_ok)
next_question()

app.exec()