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
        self.btn_borrar = QPushButton("Borrar", self)
        #Creamos otro boton para salto de texto
        self.btn_salto = QPushButton("Obtener Texto", self)
        #Movemos el boton de borrar
        self.btn_borrar.move(215, 20)
        
        #Luego creamos el text edit
        self.editor = QTextEdit(self) #la palabra self es para que aparezca el QTextEdit
        #Ahora redimensionamos nuestro TextEdit
        self.editor.resize(300, 300)
        #Tambien lo movemos
        self.editor.move(100, 100)
        
        #Ahora creamos las señales de los botones
        #Creamos la señal de borrar del boton
        self.btn_borrar.clicked.connect(self.borrar)
        #creamos la señal de saltar linea del boton
        self.btn_salto.clicked.connect(self.salto_linea)
        
    #Ahora creamos la funcion de las señales del los botones
    def borrar(self):
        self.editor.clear()
    def salto_linea(self):
        print(self.editor.toPlainText())
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec())
        
#Se puede usar este codigo para imprimir texto en otra ventana de texto                 