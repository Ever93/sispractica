from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
import sys

class VentanaBoton(QWidget):
    def __init__(self):
        super(VentanaBoton, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Ventana con boton")
        self.mostrar_botones()

    def mostrar_botones(self):
        label = QLabel(self)
        label.setText("Presiona Boton")
        label.move(100, 20)

        boton = QPushButton("Presioname", self)
        boton.move(105, 50)
        boton.clicked.connect(self.boton_presionado)

    def boton_presionado(self):
        print("Se ha cerrado la ventana")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaBoton()
    window.show()
    sys.exit(app.exec_())

#QpushButton: para dar comandos simples a la computadora
#QlineEdit: sirve para que el usuario ingrese informacion
#QcheckBox: permite hacer botones de seleccion
#QMessageBox: Para mostra cuadros de dialogo de alerta o informacion
#Entenderemos la diferencia de una ventana y un cuadro de dialogo