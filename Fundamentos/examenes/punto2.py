import os
while True:   
    numero_filas = int(input("Digite el número de filas de las matrices: "))
    numero_columnas = int(input("Digite el número de columnas de las matrices: "))
    if numero_filas < 5 or numero_columnas < 5:
        print("El programa debe funcionar para matrices que tengan 5 o más filas y columnas.")
    else:
        listA = []
        sumatoria = 0
        for i in range(0,numero_filas):
            listA.append([])
            for j in range(0,numero_columnas):
                val = float(input(f"Digite el valor de la lista A en la posición {i},{j}: "))
                listA[i].append(val)

        for j in range(1,numero_columnas):
            sumatoria = sumatoria + listA[1][j] + listA[2][j]
        for i in range(1,numero_filas):
            sumatoria = sumatoria + listA[i][1] + listA[i][3]
            
        print(sumatoria)

        respuesta = str(input("¿Desea seguir usando el programa? | 1. Si | 2. No |: ")) 
        if respuesta == "2":
            os.system("cls") 
            break  
        else:
            os.system("cls")
            




