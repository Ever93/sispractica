from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys

#Creamos nuestra clase, nombre de clase empieza con mayuscula
class Esqueleto(QWidget):
    #Definimos nuestro metodo constructor
    def __init__(self):
        super(Esqueleto, self).__init__()
        #llamamos a la funcion que inicia nuestra ventana
        self.initializate()

    #Luego definimos nuestra funcion que abre la ventana
    def initializate(self):
        #Aqui le asignamos un tamaño
        self.setGeometry(500, 500, 200, 200)#500x500 es la coordenada donde va a aparecer"
                                            #200x200 es el tamaño de la ventana
        #Tambien le asignamos un nombre a esta ventana
        self.setWindowTitle("Esqueleto animado")
        #Ocultamos la barra de nuestra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        #Mostramos esqueleto
        self.mostrar_esqueleto()
        
    #definimos la funcion que muestra el esqueleto
    def mostrar_esqueleto(self):
        esqueleto = ("esqueleto.gif")
        
        #usamos un try para mostrar la imagen
        try:
            #Abre la imagen
            with open(esqueleto):
                #Creamos aqui nuestra etiqueta
                lbl_esqueleto = QLabel(self)
                #Creamos nuestra pelicula
                movie = QMovie(esqueleto) #Definimos la variable
                #Asignamos a este esqueleto una imagen
                lbl_esqueleto.setMovie(movie) #le pasamos la variable movie
                #Iniciamos nuestro movie
                movie.start()
                
        #Creamos nuestra excepcion por si no se encuentra el archivo
        except FileNotFoundError:
            #Mostramos en pantalla de que no se encuentra el archivo
            print("No se encuentra el archivo")
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Esqueleto()
    window.show()
    sys.exit(app.exec_())
