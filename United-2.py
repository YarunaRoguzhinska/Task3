from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QHBoxLayout, QPushButton, QLineEdit

app = QApplication([])
window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(500,500)
window.move(100,100)



window.show()
app.exec_()