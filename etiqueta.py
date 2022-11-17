from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

class Applicacion(QWidget):
    def __init__(self):
        super(Applicacion, self).__init__()
        self.emptywindow()
    
    def emptywindow(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Ventana de Etiquetas")
        self.displayLabels()

    def displayLabels(self):
        texto = QLabel(self)
        texto.setText("Globo Mundial")
        texto.move(500, 15)

        image = r"world.png"
        try:
            with open(image):
                labelimage = QLabel(self)
                pixmap = QPixmap(image)
                labelimage.setPixmap(pixmap)
                labelimage.move(30, 30)
        except:
            print("No se encuentra la imagen en la ruta especificada")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Applicacion()
    window.show()
    sys.exit(app.exec_())

