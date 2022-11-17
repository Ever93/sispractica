from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap
import sys

class PerfilUsuario(QWidget):
    def __init__(self):             #Se define el metodo constructor
        super(PerfilUsuario, self).__init__()
        #Llamamos a la funcion que inicia la ventana
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle("Perfil de Usuario")
        self.mostrar_imagenes()
        self.mostrar_labels()

    def mostrar_imagenes(self):
        foto_perfil = r"Imagen/profile_image.png"
        foto_fondo = r"Imagen/skyblue.jpg"

        try:            #Para mostrar imagenes
            with open(foto_fondo):
                label_fondo = QLabel(self)
                pixmap = QPixmap(foto_fondo)
                label_fondo.setPixmap(pixmap)
        except FileNotFoundError:
            print("No se encontro la imagen")

        try:            #Para mostrar imagenes
            with open(foto_perfil):
                label_perfil = QLabel(self)
                pixmap = QPixmap(foto_perfil)
                label_perfil.setPixmap(pixmap)
                label_perfil.move(100, 25)
        except FileNotFoundError:
            print("No se encontro la imagen")

    def mostrar_labels(self):
        usuario = QLabel(self)
        usuario.setText("Ever Benitez")
        usuario.move(100, 155)
        usuario.setFont(QFont("Arial", 17))

        biografia_titulo = QLabel(self)
        biografia_titulo.setText("Biografia")
        biografia_titulo.move(15, 185)
        biografia_titulo.setFont(QFont("Arial", 15))


        biografia = QLabel(self)
        biografia.setText("Intentando desarrollar habilidades de programador")
        biografia.move(15, 220)
        biografia.setWordWrap(True)


        habilidades_titulo = QLabel(self)
        habilidades_titulo.setText("Habilidades")
        habilidades_titulo.move(15, 260)
        habilidades_titulo.setFont(QFont("Arial", 15))


        habilidades = QLabel(self)
        habilidades.setText("Tecnico Informatico, Programador Jr.")
        habilidades.move(15, 290)
        habilidades.setWordWrap(True)


        experiencia_titulo = QLabel(self)
        experiencia_titulo.setText("Experiencia")
        experiencia_titulo.move(15, 320)
        experiencia_titulo.setFont(QFont("Arial", 15))


        experiencia = QLabel(self)
        experiencia.setText("Reparacion de equipos informaticos")
        experiencia.move(15, 350)
        experiencia.setFont(QFont("Arial", 8))


        fecha = QLabel(self)
        fecha.setText("Noviembre 03 del 2022")
        fecha.move(15, 370)
        experiencia.setFont(QFont("Arial", 8))

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PerfilUsuario()
    window.show()
    sys.exit(app.exec_())

