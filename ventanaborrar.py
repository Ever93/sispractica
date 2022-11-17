from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Aplicacion principal")
        self.mostrar_widget()

    def mostrar_widget(self):
        QLabel("Escribe tu nombre", self).move(100,10)
        nombre = QLabel(self)
        nombre.setText("Nombre")
        nombre.move(70, 50)


        self.nombre_entrada = QLineEdit(self)
        self.nombre_entrada.move(13, 50)
        self.nombre_entrada.resize(200, 20)
        self.nombre_entrada.setAlignment(Qt.AlignLeft)

        self.boton = QPushButton(self)
        self.boton.move(160, 110)
        self.boton.setText("Limpiar")
        self.boton.clicked.connect(self.limpiar_line_edit)

    def limpiar_line_edit(self):
        self.nombre_entrada.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())


