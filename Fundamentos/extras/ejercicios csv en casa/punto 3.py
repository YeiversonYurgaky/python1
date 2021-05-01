#Yeiverson Yurgaky Jimenez

import csv

with open("tecno.csv") as tec:
    archivo = csv.reader(tec)

    panta_led = 0
    ubica = 0
    tera = 0
    ram = 0

    for registro in archivo:

        equi_gigas_total = int(registro[4])

        #punto A
        if registro[5] == "LED":
            panta_led = panta_led + int(registro[5])
        #punto B
        if registro[1] == "Edificio Central":
            ubica = ubica + int(registro[1])
        #punto C
        if registro[4] >= "1024Gb":
            tera = tera + int(registro[4])
            porcentaje = tera * equi_gigas_total / 100
        #punto D
        if registro[2] == "RAM en Gb":
            ram = ram + int(registro[2])
            promedio = ram / 5
    print(f"El numero de equipos que tienen pantallas LED es {panta_led}")
    print(f"El número de equipos que estan ubicados en el Edificio Central es de {ubica}")
    print(f"El porcentaje de equipos que tienen más de 1TB en disco duro es de {porcentaje}%")
    print(f"El promedio total de capacidad de RAM teniendo en cuenta 5 módulos con distinta capacidad es {promedio}")
    
   