#En esta seccion veremos detectar tecla
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        
    # ahora detectamos el teclado
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            print("Se presiono la tecla Enter")
        
        
 #Arranque
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())
            