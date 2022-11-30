#Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Suele hacer ventas
#por correo y la empresa de logistica les cobra por peso cada paquete, asi que deben calcular el peso
#de los payasos y muñecas que saldran en cada paquete a demanda. Cada payaso pesa 112g
#y cada muñeca 75g. Un cliente frecuentemente pide la cantidad de 23 payasos y 54 muñecas, realiza un 
#programa que muestre el peso total de toda la venta.
#Pista: suponiendo que un cliente pide 5 payasos y 3 muñecas, la jugueteria deberia hacer la
#multiplicacion de la cantidad de payasos con su peso, al igual que las muñecas;
#al tener ambos totales de peso, se debe sumar
cant_payaso = int(input("Total de payasos vendidos:"))
cant_muneca = int (input("Total de muñecas vendidas:"))
peso_payaso = 112
peso_muneca = 75
total = (cant_payaso*peso_payaso+cant_muneca*peso_muneca)
print(total)