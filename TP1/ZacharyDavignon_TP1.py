import sys
import os
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel
)
from PySide6.QtCore import Qt


#File Reading
json_file = sys.argv[1]
print(json_file)
json_file_size = sys.getsizeof(json_file)
try:
    file = open(json_file, encoding="utf-8")
    data = json.load(file)
    print(data)
except:
    print(f"Could not load data from {json_file}")

#Get file name
file_name = os.path.basename(json_file)



#Crée une application (Grosse boite)
app = QApplication([])

#Crée Tableau
tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(len(data[0]))
tableau.setHorizontalHeaderLabels(data[0].keys())

#Logique pour chercher et placer chaque item dans les cells
for row, cells in enumerate(data): #Pour chaque ligne, stock combien il y en a dans row et l'infortmation recu est stocké dans cells
    for col, value in enumerate(data[row].values()): ##Pour chaque cells on stock le nombre dans col et la value de chaque item json dans value
        tableau.setItem(row, col, QTableWidgetItem(str(value))) #Par rapport au nombre de colonnes et au nombre de lignes qui s'incrémente on va placer les données de value dans les cases

#Active le sorting
tableau.setSortingEnabled(True)

#Fonction pour chercher dans le fichier
def search(s):
    tableau.setCurrentItem(None) #Met le higlight a none pour causer aucun probleme

    matching_items = tableau.findItems(s,Qt.MatchFlag.MatchContains) #On regarde si un item match avec ce qu'on écrit

    if not s: #Si on trouve rien on sort de la fonction
        return
    
    if matching_items: #Si une lettre match pour tout les lettres qui match on highlight
        for item in matching_items:
            item.setSelected(True)

#Création searchbar
searchbar = QLineEdit(placeholderText="Search...")
searchbar.textChanged.connect(search)

window = QMainWindow()
container = QWidget() #Boite qui englobe notre layout
file_info = QLabel(file_name + " / " + str(json_file_size) + " bytes" + " / " +  str(len(data)) + " élements")
container_layout = QVBoxLayout()
container_layout.addWidget(searchbar)
container_layout.addWidget(tableau)
container_layout.addWidget(file_info)
container.setLayout(container_layout)
window.setCentralWidget(container)

window.show()
sys.exit(app.exec())

