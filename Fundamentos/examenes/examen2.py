import math
import os

while True:

    print("Hallar arcoseno")

    


    option2 = int(input("Como desea digitar su angulo | 1. En grados | 2. En radianes |: "))

    if option2 == 1:
        angulo = float(input("Digite el ángulo en grados: "))
        if angulo > 1:
            print("El angulo debe ser menor que 1")
        else:
            radianes = angulo*math.pi/180
                
    elif option2 == 2:
        radianes = float(input("Digite el ángulo en radianes: "))
        if radianes > 1:
            print("El angulo debe ser menor que 1")
        else:
            radianes = radianes
                   
    else:
        print("La opción digitada no existe")



    suma20211019190 = 0

    for n in range(0,20,1):
        factorial1 =1
                    
        numeradorfac = 2*n

        for i in range(1,numeradorfac+1):
            factorial1 = factorial1 * i

    for n2 in range(0,20,1):
        denominadorfac = n ** 2
        factorial2 = 1

        for i2 in range(1,denominadorfac+1):
            factorial2 = factorial2 * i2

        conversion = math.degrees(radianes)
        ang20211019190 = (factorial1 / (4**n2 * factorial2**2 * 2*n2+1)) * radianes**2*n2+1
        suma20211019190 = suma20211019190 + ang20211019190

    if option2 == 1:                                
        print(f"el arcoseno de {conversion} grados es: {suma20211019190:.3f} según la serie de McLaurin, y según los métodos de python es de {math.asin(radianes):.3f}")

    else:
        print(f"el arcoseno de {radianes} radianes es: {suma20211019190:.3f} según la serie de McLaurin, y según los métodos de python es de {math.asin(radianes):.3f}")
   
       

    respuesta = str(input("¿Desea seguir usando la calculadora? | 1. Si | 2. No |: ")) 
    if respuesta == "2":
        os.system("cls") 
        break  
    else:
        os.system("cls") 
        
"""
an = float(input("a: "))

sumatoria = 0

for n in range(0,20,1):
    factorial1 =1
    factorial2 = 1
    numeradorfac = 2*n
    denominadorfac = n ** 2

    for i in range(1,numeradorfac+1,):
        factorial1 = factorial1 * i

    for i2 in range(1,denominadorfac+1,):
        factorial2 = factorial2 * i2

    arcosen = factorial1 * an** 2*n+1 / 4**n * factorial2**2 * 2*n+1 
    sumatoria = sumatoria + arcosen

print(sumatoria)
print(arcosen)
print(factorial1)
print(factorial2)
"""
        