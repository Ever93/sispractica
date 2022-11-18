#El textEdit nos permite ingresar parrafos
#Tambien es util para reproducir listas y tablas
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()
        
    def initialize(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("QTextEdit")
        self.display_widgets()
        
    def display_widgets(self):
        #Aqui creamos el boton de borrar
            