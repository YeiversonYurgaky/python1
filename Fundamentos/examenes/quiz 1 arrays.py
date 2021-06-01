"""
Crear un programa en Python que a partir de una lista llama lista_A de 10 elementos cree 3 listas más así:
1. Lista que contenga los elementos múltiplos de 2
2. Lista que contenga los factoriales de los elementos de la lista_A
3. Lista que contenga los elementos de la lista_A ubicados en las posiciones impares
El usuario podrá escoger cuál de las opciones ejecutar.
"""
import os

while True:

    print("""¿Que desea evaluar?
    1. Lista que contenga los elementos múltiplos de 2
    2. Lista que contenga los factoriales de los elementos de la lista_A
    3. Lista que contenga los elementos de la lista_A ubicados en las posiciones impares
    """)

    option = int(input("Digite la opcción que desea evaluar: "))

    if option == 1:

        lista_A = []

        for i in range(0,10):
            valor = int(input(f"Digite el valor de la posición {i}: "))
            lista_A.append(valor)

        for i in range(0,10):
            if lista_A[i] % 2 == 0:
                print(f"Los multiplos de 2 son: {lista_A[i]}")

    elif option == 2:
        lista_A = []
        lista_B = []
        
        for i in range(0,10):
            valor = int(input(f"Digite el valor de la posición {i}: "))
            lista_A.append(valor)
       
        for i in range(0,10):
            factorial = 1 
            
            for j in range(1,lista_A[i]+1):
                factorial = factorial * j
            lista_B.append(factorial)
            
        print(f"Los factoriales de los elementos de la lista son: {lista_B[:]}")

    elif option == 3:
        lista_A = []
        for i in range(0,10):
            valor = int(input(f"Digite el valor de la posición {i}: "))
            lista_A.insert(i, valor)

        for i in range(0,10):  
            if i % 2 != 0 and i != 0:
                print(f"Los elementos ubicados en las posiciones impares son: {lista_A[i]}")

    respuesta = str(input("¿Desea seguir usando la calculadora? | 1. Si | 2. No |: "))
    if respuesta == "2":
        os.system("cls") #para poder limpiar pantalla
        break  
    else:
        os.system("cls") #para poder limpiar pantalla