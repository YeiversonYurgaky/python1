option = int(input("Digite la opción 1: Áreas, 2: Volúmenes, 3: Perímerto: "))

if option == 1:
    opc2 = int(input("Digite 1 para cuadrado o 2 para circulo: "))
    
    if opc2 ==1:
        lado = float(input("Digite el valor del lado: "))
        area = lado * lado
        print("El area solicitada es: "+str(area))

    elif opc2==2:
        radio = float(input("Digite el radio del círculo"))
    pi = 3.1416
    area = pi * pow(radio,2)
    print("El area solicitada es: "+str(area))


    else:
        print("La opción de área no existe")

elif option == 2:
    opc2 = int(input("Digite 1 para esfera o 2 para cubo: "))
    
    if opc2 ==1:
        radio = float(input("Digite el valor del radio de la esfera: "))
        pi = 3.1416
        vol = 3/4*pi*pow(radio,3)
        print("El volumen es: ",vol)
    elif opc2==2:
        lado = float(input("Digite el valor del lado: "))
        vol = lado * lado * lado
        print("El volumen es de: ",vol)
    else:
        print("La opción de volumen no existe")
    
elif option == 3:opc2 = int(input("Digite 1 para cuadrado o 2 para circunferencia: "))
    
    if opc2 ==1:
        lado = float(input("Digite el valor del lado: "))
        per = 4*lado
        print("El perímetro es de: ",per)

    elif opc2==2:
        radio = float(input("Digite el valor del radio de la esfera: "))
        pi = 3.1416
        per = 2 * pi * radio
        print("El perímetro es: ",per)
        else:
        print("La opción de perímetro no existe")
    
else:
    print("Lo siento, esa opción no existe")