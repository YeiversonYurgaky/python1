#hallar areas, escoge figura: 1 triangulo, 2 circulo, 3 reactangulo

option = int(input("Digite la opción 1: Área triángulo, 2: Área círculo, 3: Área rectángulo: "))

if option == 1:
    base = float(input("Digite la base del triágulo"))
    alt = float(input("Digite la altura del triágulo"))
    area = base*alt/2
    print("El area solicitada es: "+str(area))
elif option == 2:
    radio = float(input("Digite el radio del círculo"))
    pi = 3.1416
    area = pi * pow(radio,2)
    print("El area solicitada es: "+str(area))
elif option == 3:
    base = float(input("Digite la base del rectágulo"))
    alt = float(input("Digite la altura del rectágulo"))
    area = base * alt
    print("El area solicitada es: "+str(area))
else:
    print("Lo siento, esa opción no existe")

