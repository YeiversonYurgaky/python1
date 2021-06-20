#Yeiverson Yutgaky Jimenez

import os
while True: 
    dimencion = int(input("Digite el número de elementos para ambas listas: "))
    listA = []
    listB = []
    listC = []
    suma = 0
    for i in range(0,dimencion):
        val = int(input(f"Digite los valores de la lista A en la posición {i}: "))
        listA.append(val)
    for i in range(0,dimencion):
        val2 = int(input(f"Digite los valores de la lista B en la posición {i}: "))
        listB.append(val2)
    for i in range(0,dimencion):
        suma = listA[i] + listB[i]
        factorial = 1
        for j in range(1,suma+1):
            factorial = factorial*j
        listC.append(factorial)
    print(listC[:])

    respuesta = str(input("¿Desea seguir usando el programa? | 1. Si | 2. No |: ")) 
    if respuesta == "2":
        os.system("cls") 
        break  
    else:
        os.system("cls")