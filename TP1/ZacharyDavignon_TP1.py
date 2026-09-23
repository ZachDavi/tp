import sys

json_file = sys.argv[1]


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

#Crée une application (Grosse boite)
app = QApplication([])

window = QMainWindow()
window.show()
sys.exit(app.exec())

