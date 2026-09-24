import sys
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)



json_file = sys.argv[1]
print(json_file)

try:
    file = open(json_file, encoding="utf-8")
    data = json.load(file)
    print(data)
except:
    print(f"Could not load data from {json_file}")

for i in data:
    print("Keys\n")
    for k in i.keys():
        print(f"      -{k}")
    print("\n")
    print("Values\n")
    for v in i.values():
        print(f"      -{v}")
    print("\n")
    print("Items\n")
    for e in i.items():
        print(f"      -{e}")
    print("\n")
    


#Crée une application (Grosse boite)
app = QApplication([])
layout = QHBoxLayout()
tableau = QTableWidget()
searchbar = QLineEdit(placeholderText="Search...")
tableau.setRowCount(len(data))
tableau.setColumnCount(len(data[0]))
tableau.setHorizontalHeaderLabels(data[0].keys())

layout.addWidget(searchbar)
layout.setSpacing(20)
layout.addWidget(tableau)

for row, cells in enumerate(data):
    for col, value in enumerate(data[row].values()):
        tableau.setItem(row, col, QTableWidgetItem(str(value)))


tableau.setSortingEnabled(True)
window = QMainWindow()
window.setLayout(layout)
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())

