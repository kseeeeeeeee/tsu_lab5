import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Простейшее приложение PyQt5")
window.setGeometry(100, 100, 350, 200)

label = QLabel("Добро пожаловать в PyQt5!")

button = QPushButton("Нажми меня")


def show_message():
    label.setText("Привет! Это приложение на PyQt5.")


button.clicked.connect(show_message)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
