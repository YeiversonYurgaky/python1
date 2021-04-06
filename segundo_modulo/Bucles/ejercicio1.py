"""
  Escriba un programa que pida dos números enteros y escriba qué 
    números impares desde el primero hasta el segundo. (+5)
"""
numero1 = int(input("Digite el primer número entero: "))
numero2 = int(input("Digite el segundo número entero: "))

for i in range(numero1,numero2+1):
    if i % 2 != 0:

        print(i)
