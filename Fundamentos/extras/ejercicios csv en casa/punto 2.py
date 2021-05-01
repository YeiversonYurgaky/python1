#Yeiverson Yurgaky Jimenez

import csv

with open("materias.csv") as mt:
    archivo = csv.reader(mt)

    materias = 0
    credi_total_teo = 0
    credi_total_prac = 0
    credi_contadu = 0
    materias_pacti = 0






    for registro in archivo:

        total_materias = int(registro[1])

        #punto A
        if registro[2] == "Tecnología en Sistemas" and registro[4] == "Primer Semestre":
            print(f"Las materias de Tecnología en Sistemas en el Primer Semestre son: {registro[1]}")
        #punto B
        if registro[5] == "Teórica":
            credi_total_teo = credi_total_teo + int(registro[3])
        #punto C        
        if registro[5] == "Práctica":
            credi_total_prac = credi_total_prac + int(registro[3])
            promedio_prac = credi_total_prac / int(registro[1])
        #punto D
        if registro[2] == "Contaduría Pública":
            credi_contadu = credi_contadu + int(registro[3])
            porcen_contadu = credi_contadu * int(registro[3]) / 100
        #punto E
        if registro[5] == "Práctica":
            materias_pacti = materias_pacti + int(registro[1])
            porcen_pacti = materias_pacti * total_materias / 100

    print(f"El número de créditos total de las materias que son de tipo Teórica es de {credi_total_teo}")
    print(f"El promedio de los créditos de las materias de tipo Práctica es {promedio_prac}")
    print(f"El porcentaje de créditos de las materias del programa de Contaduría Pública es {porcen_contadu}")
    print(f"El porcentaje de materias prácticas con respecto al total es de {porcen_pacti}")






