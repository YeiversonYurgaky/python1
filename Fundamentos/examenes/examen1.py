print("****CALCULADORA BÁSICA****")

option = int(input("Elaija una opción |1. Suma|2.Resta|3.Multiplicación|4.División|5. Exponeciación|: "))

if option == 1:
    dato1 = float(input("Digite el valor del dato 1: "))
    dato2 = float(input("Digite el valor del dato 2: "))
    suma = dato1 + dato2
    print("El resultado de la suma es: ",suma)

elif option == 2:
    dato1 = float(input("Digite el valor del dato 1: "))
    dato2 = float(input("Digite el valor del dato 2: "))
    resta = dato1 - dato2
    print("El resultado de la resta es: ",resta)

elif option == 3:
    dato1 = float(input("Digite el valor del dato 1: "))
    dato2 = float(input("Digite el valor del dato 2: "))
    multiplicación = dato1 * dato2
    print("El resultado de la multiplicación es: ",multiplicación)

elif option == 4:
    dato1 = float(input("Digite el valor del dato 1: "))
    dato2 = float(input("Digite el valor del dato 2: "))
    if dato2 == 0:
        print("NO")
    else:

        resultado = dato1 / dato2
        print("El resultado de la división es: ",resultado)

elif option == 5:
    dato1 = float(input("Digite el valor de la base: "))
    dato2 = float(input("Digite el valor de la potencia: "))
    exponenciacón = pow(dato1,dato2)
    print("El resultado de la exponenciación es: ",exponenciacón)

else:
    print("Esa opción no existe")
    





