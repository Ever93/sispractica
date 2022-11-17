#Crea un programa que le pida al usuario un numero de horas de trabajo diarios y una tarifa por hora para calcular el salario
#Al final imprimir el salario
horas = int(input("Ingresa la cantidad de horas trabajadas: "))
tarifa = float(input("Ingresa el salario por horas: "))
salario = horas * tarifa
print("El salario del dia es: ", salario)