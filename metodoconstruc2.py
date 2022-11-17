class Celular:
    variable1 = "Ejemplo"

    def __init__(self, color):         #Definimos funcion
        self.color = color    #La palabra self se utiliza para hacer referencia al objeto

    def encender(self, contrasena):         #definimos un metodo
        print("Encendiendo telefono", contrasena)
        print(self.color)

    def apagar(self):
        print("Apagando telefono")

#Ahora vamos a instanciar el objeto para llamar a sus metodos y funciones

objeto_celular = Celular("Blanco")
print(objeto_celular.color)
#Ahora llamamos al metodo encender
objeto_celular.encender("ever1010")