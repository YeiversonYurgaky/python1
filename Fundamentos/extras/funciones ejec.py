#Yeiverson Yurgaky Jimenez

import os

def sumar (num1,num2):
    suma = num1 + num2
    return suma

def restar (num1,num2):
    resta = num1 - num2
    return resta

def multiplicacion(num1,num2):
    multi = num1 * num2
    return multi

def division(num1,num2):
    divi = num1 / num2
    return divi

def potencia(num1,num2):
    pote = num1 ** num2
    return pote

def main():

    while True:

        print(""" 
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Potencia     
        """)
        
        op = int(input("Elija que operación desea evaluar: "))

        if op == 1:
            num1 = float(input("Digite el primer número: "))
            num2 = float(input("Digite el segundo número: "))
            print(sumar(num1,num2))
        
        elif op == 2:
            num1 = float(input("Digite el primer número: "))
            num2 = float(input("Digite el segundo número: "))
            print(restar(num1,num2))

        elif op == 3:
            num1 = float(input("Digite el primer número: "))
            num2 = float(input("Digite el segundo número: "))
            print(multiplicacion(num1,num2))
        
        elif op == 4:
            num1 = float(input("Digite el dividendo: "))
            num2 = float(input("Digite el divisor: "))
            if num2 == 0:
                print("El divisor no puede ser 0, ya que el resultado es indeterminado")
            else:
                print(division(num1,num2))
        
        elif op == 5:
            num1 = int(input("Digite la base: "))
            num2 = int(input("Digite el exponente: "))
            print(potencia(num1,num2))

        else:
            print("Digito una opción que no existe")
        
        respuesta = str(input("¿Desea seguir usando la calculadora? | 1. Si | 2. No |: ")) 
        if respuesta == "2":
            os.system("cls") 
            break

        else:
            os.system("cls") 

main()