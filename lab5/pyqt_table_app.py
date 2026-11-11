import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLabel
)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Таблица на PyQt5")
window.setGeometry(100, 100, 450, 300)

label = QLabel("Таблица успеваемости студентов")

table = QTableWidget()
table.setRowCount(4)
table.setColumnCount(3)

table.setHorizontalHeaderLabels(
    ["Имя", "Предмет", "Оценка"]
)

data = [
    ["Анна", "Математика", "5"],
    ["Иван", "Информатика", "4"],
    ["Мария", "Физика", "5"],
    ["Петр", "История", "3"]
]

for row in range(4):
    for column in range(3):
        item = QTableWidgetItem(data[row][column])
        table.setItem(row, column, item)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(table)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
