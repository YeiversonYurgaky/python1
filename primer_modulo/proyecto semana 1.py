"""

crear un programa que le pida al usuario su edad, nombre, dos números y muestre por pantalla:



    - suma

    - resta

    - multiplicación

    - o división (dependiendo de la opcion)

    - de ambos números seguidos de su nombre y edad



    NOTA: si el usuario no es mayor de 5 años, no puede usar el programa

"""
"""
print("****CALCULADORA BÁSICA****")

edad = int(input("Digite su edad: "))

if edad < 5:
    print("No puedes usar este programa si es menor de 5 años")

else:

    nombre = str(input("Digite su nombre: "))

    dato1 = float(input("Digite el valor del dato 1: "))
    dato2 = float(input("Digite el valor del dato 2: "))

    option = int(input("Elaija una opción |1. Suma|2.Resta|3.Multiplicación|4.División|: "))

    if option > 4:
        print("Opción invalida")

    else:

         if option == 1:
            resultado = dato1 + dato2
        
         elif option == 2:
            resultado = dato1 - dato2
        
         elif option == 3:
            resultado = dato1 * dato2
        
         elif option == 4:

            if dato2 != 0:
                resultado = dato1 / dato2  
                
            else:
                print("El divisor no puede ser 0")
                 
         print(f"El resultado de la operación con los números {dato1} y {dato2}|{nombre}|{edad} años, es: {resultado}")
"""
print("****CALCULADORA BÁSICA****")

edad = int(input("Digite su edad: "))

if edad < 5:
    print("No puedes usar este programa si es menor de 5 años")

else:

    nombre = str(input("Digite su nombre: "))

    option = int(input("Elija una opción |1. Suma|2.Resta|3.Multiplicación|4.División|: "))

    if option == 1:
        dato1 = float(input("Digite el valor del dato 1: "))
        dato2 = float(input("Digite el valor del dato 2: "))
        suma = dato1 + dato2
        print(f"El resultado de la operación con los números {dato1} y {dato2}|{nombre}|{edad} años, es: {suma}")

    elif option == 2:
        dato1 = float(input("Digite el valor del dato 1: "))
        dato2 = float(input("Digite el valor del dato 2: "))
        resta = dato1 - dato2
        print(f"El resultado de la operación con los números {dato1} y {dato2}|{nombre}|{edad} años, es: {resta}")

    elif option == 3:
        dato1 = float(input("Digite el valor del dato 1: "))
        dato2 = float(input("Digite el valor del dato 2: "))
        multiplicación = dato1 * dato2
        print(f"El resultado de la operación con los números {dato1} y {dato2}|{nombre}|{edad} años, es: {multiplicación}")

    elif option == 4:
        dato1 = float(input("Digite el valor del dividendo: "))
        dato2 = float(input("Digite el valor del divisor: "))
        if dato2 == 0:
            print("El divisor no puede ser 0")
        else:
            divison = dato1 / dato2
            print(f"El resultado de la operación con los números {dato1} y {dato2}|{nombre}|{edad} años, es: {divison}")

    else:
        print("Esa opción no existe")

    


