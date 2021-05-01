#Yeiverson Yurgaky Jimenez

import csv

with open("dimayor.csv") as dm:
    archivo = csv.reader(dm)

    tarjeama = 0
    tarjerojas = 0
    jugadores = 0
    jugadores2 = 0
    totaltarj = 0
    jugadores_singol = 0

    for registro in archivo:
        #punto A
        if int(registro[4]) == 0:
            tarjeama = tarjeama + 1
            
        #punto B
        for i in range(registro[5]):
            tarjerojas = tarjerojas + i
        
        #punto C
        if int(registro[3]) >= 1:
            for j in range(registro[3]):
                jugadores = jugadores + j
           
            
        if int(registro[3]) >= 15:
            for k in range(registro[3]):
                jugadores2 = jugadores2 + k

        #punto D
        if (registro[2]) == "Deportes Tolima":

            totaltarj = totaltarj + int(registro[4])

        #punto E
        if int(registro[3]) == 0:
            jugadores_singol = jugadores_singol + 1
            porcentaje = jugadores_singol * jugadores / 100

    print(f"El numero de jugadores que nunca le han sacado tarjeta amarilla es {tarjeama}")
    print(f"El número de tarjetas rojas sacadas en este año es de {tarjerojas}")
    print(f"El número de jugadores que marcaron al menos 1 gol es {jugadores}")
    print(f"El número de jugadores que marcaron más de 15 goles es {jugadores2}")
    print(f"El Deportes Tolima tiene un total de {totaltarj} tarjetas amarillas")
    print(f"El porcentaje de jugadores que no anotaron ningún gol es de {porcentaje}%")



