class Celular:
    def __init__(self, color, almacenamiento):      
        self.color = color
        self.almacenamiento = almacenamiento

    def informacion(self):      #metodo
        print("Color ", self.color)
        print("Almacenamiento ", self.almacenamiento,"GB")

    def encender(self):
        print("Encendiendo Telefono")

    def apagar(self):
        print("Apagando telefono")

#Crear la clase padre llamando a sus atributos
#Creamos una subclase
class Android(Celular):
    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento de celular")

class Iphone (Celular):
    def transferir_archivos(self):
        print("Transfiriendo archivos a la computadora")

#Instanciar las clases para crear objetos tipo android y tipo iphone

celular_android = Android("Blanco", 64)
celular_android.expandir_almacenamiento()
celular_android.informacion()