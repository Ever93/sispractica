from PyQt5.QtWidgets import QApplication, QWidget
import sys

class VentanaVacia (QWidget):
    def __init__(self):
        super(VentanaVacia, self).__init__()
        self.initializeUi()


    def initializeUi(self):
        #Definir de que tamaño sera nuestra ventana
        self.setGeometry(100, 100, 400, 600)            #Los dos parametros 100,100 indica donde se inicia la ventana
        #Ttitulo de la ventana
        self.setWindowTitle("Ventana Principal")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = VentanaVacia()
    Window.show()
    sys.exit(app.exec_())


#Sys: usamos este modulo para pasar argumentos de linea de comando a nuestras aplicaciones y cerrarlas. sys.exit(app.exec_())
#QtWidgets: este modulo proporciona elementos de la interfaz de usuario para crear GUIS de escritorio
#Qapplication: Gestiona el bucle de eventos principal, la inicializacion y finalizacion de la aplicacion

