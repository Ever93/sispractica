from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class RegistroUsuario(QWidget):
    def __init__(self):
        super(RegistroUsuario, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Registro Usuario")
        self.display_widgets()

    #Aqui vamos a crear todos los widgets que se usara para recoger
    #los datos del 
    def display_widgets(self):
        #Creamos una variable para agregar la imagen
        user_image = "nuevo_usuario.png"
        #usamos un try para insertar la imagen
        try:
            with open(user_image):
                #creamos la etiqueta para la imagen
                etiqueta_imagen = QLabel(self)
                #Creamos nuestro Pixmap y le pasamos nuestra imagen
                pixmap = QPixmap(user_image)
                etiqueta_imagen.setPixmap(pixmap)
                #por ultimo movemos nuestra etiqueta
                etiqueta_imagen.move(175, 80)
        except FileNotFoundError:
            print("No se encuentra el archivo")

        #Ahora creamos la etiqueta que dira crear nueva cuenta
        etiqueta_login = QLabel("Crear Nueva Cuenta", self)
        #Movemos la etiqueta a su ubicacion
        etiqueta_login.move(0, 20)
        #Colocamos una fuente al texto
        etiqueta_login.setFont(QFont("Arial", 20))
        #Ahora asignamos un tamaño
        etiqueta_login.resize(400, 40)
        #Ahora alineamos el texto al centro
        etiqueta_login.setAlignment(Qt.AlignCenter)


        #Ahora creamos la etiqueta de nombre de usuario y lineedit
        self.etiqueta_nombre = QLabel("Nombre de usuario:", self)
        #Movemos la etiqueta
        self.etiqueta_nombre.move(30, 180)

        #Creamos el LineEdit donde se va a ingresar los datos
        self.entrada_nombre = QLineEdit(self)
        self.entrada_nombre.move(150, 180)
        #Tambien le asignamos un tamaño a nuestro LineEdit
        self.entrada_nombre.resize(200, 20)

        #Creamos otra etiqueta para nombre completo
        self.etiqueta_nombre = QLabel("Nombre Completo:", self)
        self.etiqueta_nombre.move(30, 210)

        #Creamos otro LineEdit para nombre completo
        self.entrada_completo = QLineEdit(self)
        self.entrada_completo.move(150, 210)
        self.entrada_completo.resize(200, 20)

        #Ahora creamos la etiqueta para la contraseña
        self.etiqueta_password = QLabel("Contraseña:", self)
        self.etiqueta_password.move(30, 240)

        #Creamos otro LineEdit para la contraseña
        self.lned_password = QLineEdit(self)
        #Al momento de ingresar texto por lineEdit que sea del tipo contraseña
        self.lned_password.setEchoMode(QLineEdit.Password)
        self.lned_password.move(150, 240)
        self.lned_password.resize(200, 20)

        #Creamos la etiqueta para confirmar la etiqueta
        self.confirmar = QLabel("Confirmar", self)
        #Movemos la etiqueta
        self.confirmar.move(30, 270)

        #Ahora creamos un lineEdit para confirmar la contraseña
        self.lned_confirmar = QLineEdit(self)
        self.lned_confirmar.setEchoMode(QLineEdit.Password)
        self.lned_confirmar.move(150, 240)
        self.lned_confirmar.resize(200, 20)

        #Creamos un boton para confirmar el registro
        self.boton_registro = QPushButton("Registrarse", self)
        #Asignamos un tamaño
        self.boton_registro.resize(200, 40)
        self.boton_registro.move(100, 310)

        #Crear la señal del boton
        self.boton_registro.clicked.connect(self.registro)

    #Definimos la funcion del boton
    def registro(self):
        #En esta seccion vamos a programar todo lo que queremos que haga el boton
        #Compararemos si coinciden los textos ingresados en LineEdit
        texto_password = self.lned_password.text()
        password_confirmar = self.lned_confirmar.text()


    #Ahora vamos a crear una condicion que muestre un cuadro de dialogo si no se cumple la condicion
        if texto_password != password_confirmar:
            #Si el password a confirmar es diferente a texto password,lanzamos una ventana de advertencia
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden,"
                                        "por favor vuelva a intentarlo", QMessageBox.ok, QMessageBox.ok)
        else:
            #Usamos a+ para saber que queremos escribir en el archivo
            with open("usuario.txt", "a+") as f:
                f.write(self.entrada_nombre.text() + "")
                #despues creamos otro para la contraseña donde ya no usamos self porque ya lo definimos arriba
                # usamos \n para indicar un salto de linea
                f.write(texto_password + "\n")
                #Despues solo tendriamos que cerrar la aplicacion
            self.close()
    
#Por ultimo corremos el programa
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroUsuario()
    window.show()
    sys.exit(app.exec_())
    #Despues creamos otra ventana