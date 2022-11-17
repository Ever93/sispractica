from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class RegistroUsuario(QWidget):
    def __init__(self):
        super(RegistroUsuario, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Registro Usuario")
        self.display_widgets()

    #Aqui vamos a crear todos los widgets que se usara para recoger
    #los datos del 
    def display_widgets(self):
        #Creamos una variable para agregar la imagen
        user_image = "nuevo_usuario.png"
        #usamos un try para insertar la imagen
        try:
            with open(user_image)