from PyQt5.QtWidgets import QCheckBox, QLabel, QApplication, QWidget
from PyQt5.QtCore import Qt                 #Qt sirve para alinear el texto
import sys

class Casilla(QWidget):
    def __init__(self):                      #Definimos el metodo constructor
        super(Casilla, self).__init__()
        self.initialize()

    #En esta linea definimos la funcion initialize
    def initialize(self):
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle("Ventana de seleccion")
        self.mostrar_widget()

    #En esta linea definimos la funcion mostrar_widget
    def mostrar_widget(self):
        label = QLabel("¿Que tipo de Helado quieres?", self)
        label.resize(250, 60)
        label.setAlignment(Qt.AlignCenter)

        vainilla = QCheckBox("Vainilla", self)
        vainilla.move(20, 80)

        fresa = QCheckBox("Fresa", self)
        fresa.move(20, 100)

        chocolate = QCheckBox("Chocolate", self)
        chocolate.move(20, 120)

        #creamos las señales
        #StateChanged verifica si la casilla esta seleccionada o deseleccionada
        vainilla.stateChanged.connect(self.imprimir_terminal)
        fresa.stateChanged.connect(self.imprimir_terminal)
        chocolate.stateChanged.connect(self.imprimir_terminal)
    #Usaremos el metodo sender para saber que casilla fue seleccionada
    def imprimir_terminal(self, estado):    #estado de la casilla
        sender = self.sender()
        if estado == Qt.Checked:
            print (f"La casilla {sender.text()} ha sido seleccionado")  #se usa la f antes de la comilla para concatenar
        else:
            print (f"La casilla {sender.text()} ha sido deseleccionado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Casilla()
    window.show()
    sys.exit(app.exec_())