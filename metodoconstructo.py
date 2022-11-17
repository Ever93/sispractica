class Celular:
    variable1 = "Ejemplo"

    def __init__(self):         #Definimos funcion
        self.color = "Rojo"     #La palabra self se utiliza para hacer referencia al objeto

    def encender(self):         #definimos un metodo
        print("Encendiendo Telefono")

    def apagar(self):
        print("Apagando telefono")

#Ahora vamos a instanciar el objeto para llamar a sus metodos y funciones

objeto_celular = Celular()
print(objeto_celular.color)
#Ahora llamamos al metodo encender
objeto_celular.encender()
