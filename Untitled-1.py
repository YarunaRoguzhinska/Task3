from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QHBoxLayout, QRadioButton, QMessageBox

dodatok = QApplication([])
vikno = QWidget()
vikno.setWindowTitle("Лотерея")
vikno.resize(500,500)
vikno.move(100,100)

def show_win():
    vic = QMessageBox()
    vic.setText("Вірно!\n Ви виграли гіроскутер")
    vic.exec_()
def show_lose():
    vic = QMessageBox()
    vic.setText("Невірно!\n Ви просто лох")
    vic.exec_()

text= QLabel()
text.setText("В якому році канал отримав золоту кнопку?")

but1=QRadioButton()
but1.setText("2015")
but2=QRadioButton()
but2.setText("2013")
but3=QRadioButton()
but3.setText("2005")
but4=QRadioButton()
but4.setText("2001")

lineV=QVBoxLayout()
lineH1= QHBoxLayout()
lineH2= QHBoxLayout()
lineV.addWidget(text, alignment = Qt.AlignCenter)

lineH1.addWidget(but1, alignment = Qt.AlignCenter)
lineH1.addWidget(but2, alignment = Qt.AlignCenter)

lineH2.addWidget(but3, alignment = Qt.AlignCenter)
lineH2.addWidget(but4, alignment = Qt.AlignCenter)

lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
vikno.setLayout(lineV)
but1.clicked.connect(show_win)
but2.clicked.connect(show_lose)
but3.clicked.connect(show_lose)
but4.clicked.connect(show_lose)

vikno.show()
dodatok.exec_()
