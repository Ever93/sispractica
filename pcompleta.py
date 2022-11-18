from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont
import sys

#Creamos la clase
class Aplicacion(QWidget):
    #Definimos el metodo constructor
    def __init__(self):
        super(Aplicacion, self).__init__()
        #creamos la funcion para iniciar la aplicacion
        self.initialize()
        
    #Definimos la funcion para iniciar la aplicacion
    def initialize(self):
        #Asignamos un tamaño
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("Minimizar ventana")
        self.display_widgets()
        
    #Definimos la funcion para display_widgets
    def display_widgets(self):
        #Creamos un boton
        self.boton = QPushButton("-", self)
        #Agregamos una fuente al boton
        self.boton.setFont(QFont("Arial", 20))
        #Asignamos un tamaño al boton
        self.boton.resize(50, 40) #Ancho por alto
        #Por ultimo movemos el boton a su ubicacion
        self.boton.move(40, 40)
        
        #creamos otro boton para maximizar
        self.boton_maximizar = QPushButton("+", self)
        self.boton_maximizar.setFont(QFont("Arial", 20))
        self.boton_maximizar.resize(50, 40)
        self.boton_maximizar.move(100, 100)
        
        #Creamos otra señal para el boton maximizar
        self.boton_maximizar.clicked.connect(self.maximizado)
        
        #Ahora creamos la señal para el boton
        self.boton.clicked.connect(self.minimizado)
        
    #Definimos la funcion minimizado para el boton
    def minimizado(self):
        self.showMinimized()
        
    #Definimos otra funcion para maximizado
    def maximizado(self):
        self.showMaximized()
        
#Por ultimo creamos un metodo de salida limpia
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())