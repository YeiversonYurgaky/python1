'''Escriba un programa que pida números decimales

    mientras el usuario escriba número mayores que el primero. (+3)'''

numero1 = float(input("Digite el primer número decimal: "))
numero2 = float(input("Digite el segundo número decimal: "))

while numero2 < numero1:
    numero2 = float(input("POR FAVOR digite un número decimal mayor que el primero: "))

print(numero2)