from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys

class Pelicula(QWidget):
    def __init__(self):
        super(Pelicula, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Buscador")
        self.mostrar_widget()

    def mostrar_widget(self):
        #Iniciar Widgets
        label_catalogo = QLabel("Catalogo de Peliculas", self)
        label_catalogo.move(20, 20)
        label_catalogo.setFont(QFont("Arial", 20))


        label_pelicula = QLabel("Ingrese el nombre de la pelicula", self)
        label_pelicula.move(20, 60)

        label_nombre = QLabel("Nombre", self)
        label_nombre.move(20, 90)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Nombre de la Pelicula")
        self.line_edit.move(80, 90)
        self.line_edit.resize(240, 20)


        self.boton = QPushButton("Buscar", self)
        self.boton.move(370, 460)
        self.boton.resize(150, 40)

        #Creamos la funcion para buscar
        self.boton.clicked.connect(self.mostrar_cuadro_dialogo)

    def mostrar_cuadro_dialogo(self):
        try:
            with open("Python\pelicula.txt") as f:
                peliculas = [linea.rstrip("\n") for linea in f]
        except FileNotFoundError:
            print("No se encontro la pelicula")

        if self.line_edit.text() in peliculas:
            QMessageBox().information(self, "Pelicula encontrada", "Pelicula encontrada en el catalogo", QMessageBox.ok, QMessageBox.ok)
        else:
            pelicula_no_econtrada = QMessageBox.question(self, "Pelicula no encontrada", "Pelicula no encontrada en el catalogo. \nDesea continuar", QMessageBox.Si | QMessageBox.No, QMessageBox.No)
            
            if pelicula_no_econtrada == QMessageBox.No:
                print("Cerrando la Aplicacion")
                self.close()
            else:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pelicula()
    window.show()
    sys.exit(app.exec_())
