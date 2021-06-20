#YEIVERSON YURGAKY JIMENEZ

import os
class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKCYAN = '\033[96m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'
while True:
    print(bcolors.BOLD+"Operaciones con vectores y matrices sobre algebra lineal"+bcolors.ENDC)
    print(bcolors.BOLD+"""
    Digite que desea operar 

    1. Operaciones entre vectores.
    2. Operaciones entre matrices
    """+bcolors.BOLD)

    option = int(input(bcolors.HEADER+"Elija una opción: "+bcolors.ENDC))

    if option == 1:
        print(bcolors.BOLD+"""
        Digite que desea operar 

        1. Suma de vectores.
        2. Resta de vectores.
        3. Multiplicación por un escalar.
        4. Multiplicación de vectores.
        """+bcolors.BOLD)

        option2 = int(input(bcolors.HEADER+"Elija una opción: "+bcolors.ENDC))

        #suma
        if option2==1:

            dimencion = int(input(bcolors.OKCYAN+"Digite el número de elementos para ambas listas: "+bcolors.ENDC))
            listA = []
            listB = []
            listC = []
            for i in range(0,dimencion):
                val = float(input(bcolors.OKCYAN+f"Digite los valores de la lista A en la posición {i}: "+bcolors.ENDC))
                listA.append(val)
            for i in range(0,dimencion):
                val2 = float(input(bcolors.OKCYAN+f"Digite los valores de la lista B en la posición {i}: "+bcolors.ENDC))
                listB.append(val2)
            for i in range(0,dimencion):
                listC.append(listA[i] + listB[i])
            print(listC[:])
        #resta
        elif option2==2:
            dimencion = int(input(bcolors.OKCYAN+"Digite el número de elementos para ambas listas: "+bcolors.ENDC))
            listA = []
            listB = []
            listC = []
            for i in range(0,dimencion):
                val = float(input(bcolors.OKCYAN+f"Digite los valores de la lista A en la posición {i}: "+bcolors.ENDC))
                listA.append(val)
            for i in range(0,dimencion):
                val2 = float(input(bcolors.OKCYAN+f"Digite los valores de la lista B en la posición {i}: "+bcolors.ENDC))
                listB.append(val2)
            for i in range(0,dimencion):
                listC.append(listA[i] - listB[i])
            print(listC[:])
        #escalar
        elif option2==3:
            listA = []
            listC = []
            dimencion = int(input(bcolors.OKCYAN+"Digite el número de elementos para la lista A: "+bcolors.ENDC))
            multi = float(input(bcolors.OKCYAN+"Digite el número que multiplicará la lista: "))
            for i in range(0,dimencion):
                val = float(input(bcolors.OKCYAN+f"Digite los valores de la lista A en la posición {i}: "+bcolors.ENDC))
                listA.append(val)
            for i in range(0,dimencion):
                listC.append(multi*listA[i])
            print(listC[:])
        #multiplicación
        elif option2 == 4:
            dimencion = int(input(bcolors.OKCYAN+"Digite el número de elementos para ambas listas: "+bcolors.ENDC))
            listA = []
            listB = []
            listC = []
            sumatoria = 0
            for i in range(0,dimencion):
                val = float(input(bcolors.OKCYAN+f"Digite los valores de la lista A en la posición {i}: "+bcolors.ENDC))
                listA.append(val)
            for i in range(0,dimencion):
                val2 = float(input(bcolors.OKCYAN+f"Digite los valores de la lista B en la posición {i}: "+bcolors.ENDC))
                listB.append(val2)
            for i in range(0,dimencion):
                multi = listA[i] * listB[i]
                sumatoria += multi
            print(sumatoria)
        else:
            print(bcolors.WARNING+"La opción digitada no extiste"+bcolors.ENDC)
    
    elif option == 2:
        print(bcolors.BOLD+"""
        Digite que desea operar 

        1. Suma de matrices.
        2. Resta de matrices.

        """+bcolors.BOLD)

        option2 = int(input(bcolors.HEADER+"Elija una opción: "+bcolors.ENDC))
        #suma de matrices
        if option2 == 1:
            numero_filas = int(input(bcolors.OKCYAN+"Digite el número de filas de las matrices: "+bcolors.ENDC))
            numero_columnas = int(input(bcolors.OKCYAN+"Digite el número de columnas de las matrices: "+bcolors.ENDC))

            listA = []
            listB = []
            listC = []

            for i in range(0,numero_filas):
                listA.append([])
                for j in range(0,numero_columnas):
                    val = float(input(bcolors.OKCYAN+f"Digite el valor de la lista A en la posición {i},{j}: "+bcolors.ENDC))
                    listA[i].append(val)
            for i in range(0,numero_filas):
                listB.append([])
                for j in range(0,numero_columnas):
                    val2 = float(input(bcolors.OKCYAN+f"Digite el valor de la lista B en la posición {i},{j}: "+bcolors.ENDC))
                    listB[i].append(val2)
            for i in range(0,numero_filas):
                for j in range(0,numero_columnas):
                    listC.append(listA[i][j] + listB[i][j])
            print(listC[:])
        #resta de matrices
        elif option2 == 2:
            numero_filas = int(input(bcolors.OKCYAN+"Digite el número de filas de las matrices: "+bcolors.ENDC))
            numero_columnas = int(input(bcolors.OKCYAN+"Digite el número de columnas de las matrices: "+bcolors.ENDC))

            listA = []
            listB = []
            listC = []

            for i in range(0,numero_filas):
                listA.append([])
                for j in range(0,numero_columnas):
                    val = float(input(bcolors.OKCYAN+f"Digite el valor de la lista A en la posición {i},{j}: "+bcolors.ENDC))
                    listA[i].append(val)
            for i in range(0,numero_filas):
                listB.append([])
                for j in range(0,numero_columnas):
                    val2 = float(input(bcolors.OKCYAN+f"Digite el valor de la lista B en la posición {i},{j}: "+bcolors.ENDC))
                    listB[i].append(val2)
            for i in range(0,numero_filas):
                for j in range(0,numero_columnas):
                    listC.append(listA[i][j] - listB[i][j])
            print(listC[:])
        else:
            print(bcolors.WARNING+"La opción digitada no extiste"+bcolors.ENDC)
    
    else:
        print(bcolors.WARNING+"La opción digitada no extiste"+bcolors.ENDC)
    
    respuesta = str(input("¿Desea seguir usando la calculadora de algebra lineal? | 1. Si | 2. No |: ")) 
    if respuesta == "2":
        os.system("cls") 
        break  
    else:
        os.system("cls")


