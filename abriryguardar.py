import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()
        
    def initialize(self):
        self.resize(500, 500)
        self.setWindowTitle("Abrir y guardar")
        self.display_widgets()
    
    def display_widgets(self):
        #Dentro de esta funcion creamos lo que se va a ver en nuestra ventana
        self.btn_abrir = QPushButton("Abrir", self)
        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.move(0, 50)
        
        #Creamos la señal del boton
        self.btn_abrir.clicked.connect(self.open)#open sera la funcion donde se conecta el boton
        self.btn_guardar.clicked.connect(self.save)
        
    #Definimos la funcion open al cual se conecta btn_abrir
    def open(self):
        file_name = QFileDialog.getOpenFileName(self, "Abrir archivos""../../../../Taller/Desktop", "ALLFiles(*);; Archivo de texto(*.txt)")
      
    def save(self):
       file_name = QFileDialog.getSaveFileName(self, "Abrir archivos""../../../../Taller/Desktop",
                                               "ALLFiles(*);; Archivo de texto(*.txt)")     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())