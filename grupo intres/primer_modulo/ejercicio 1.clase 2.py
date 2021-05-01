"""
Realizar un programa que reciba dos datos por teclado y que devuelva la suma de ambos 
"""

#numero1 = float(input("Digite el primer número: "))
#numero2 = float(input("Digite el segundo número: "))

#total = numero1 + numero2
#print("El resultado es de",total)
"""
un programa que pida dos números y que muestre cuál es mayor, cuál es menor o si son iguales (+3)
"""

dato1 = float(input("Digite el dato 1: "))
dato2 = float(input("Digite el dato 2: "))

if dato1 > dato2:
    print(dato1,"es mayor que",dato2)
else:
    print(dato2,"es menor que",dato1)

if dato1 == dato2:
    print(dato1,"es igual que",dato2)
