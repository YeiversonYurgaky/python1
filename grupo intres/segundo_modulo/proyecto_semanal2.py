'''
Escriba un programa que pida la cantidad de números que se tienen que escribir
y a continuación pida números hasta que la cantidad de elementos especificada. Mostrar la cantidad de numeros
positivos, negativos, pares e impares.
'''
import os

while True:
    perdir_num = int(input("Digite la cantidad de números que desea evaluar: "))

    if perdir_num < 0:
        print("No puede digitar valores negativos, tampoco decimales")

    else:
        sumatoria1 = 0
        sumatoria2 = 0
        sumatoria3 = 0
        sumatoria4 = 0

        for numeros in range(perdir_num):
            numeros = float(input("Digite los números que quiere comparar: "))

            if numeros > 0:
                sumatoria1 += 1
                

                if numeros % 2 == 0:
                    sumatoria2 += 1
                    

                else:
                    sumatoria3 += 1
                    

            elif numeros < 0:
                sumatoria4 += 1

        print("La cantidad de números positivos es",sumatoria1)
        print("La cantidad de números negativos es ",sumatoria4)
        print("La cantidad de números pares es",sumatoria2)
        print("La cantidad de números impares es",sumatoria3)

        respuesta = str(input("¿Desea seguir usando el programa? | 1. Si | 2. No |: ")) #controlador de flujo
        if respuesta == "2":
            os.system("cls") #para poder limpiar pantalla
            break  
        else:
            os.system("cls") #para poder limpiar pantalla
    
