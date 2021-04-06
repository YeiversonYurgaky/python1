#Yeiverson Yurgaky Jimenez

print("Programas de la Universidad de Innovación de Medellín")

option = int(input("Elija el progrma que desea cursar: |1. Ingeniería de sistemas: $2.000.000|2. Ingeniería electronica: $2.300.000|3. Ingeniería mecatrónica $4.500.000|4. Ingeniería de sistemas complejos: $3.500.000: "))

if option == 1:
    base = 2000000
    print("El programa de ingeniería de sistemas tiene un costo de $",base)

    option2 = int(input("Elija su estrato: |1|2|3|4|5|6|: "))

    if option2 >= 1 and option2 <= 3:

            #Se hace el descuento restando la cifra que resulte de la multiplicación de la base por el 5%

        descuento = base*0.05
        base = base - descuento
        print("Ya que su estrato esta entre 1 y 3 obtendra un descuento de $",descuento,". Su valor total seria de $",base)
    
    elif option2 >= 4 and option2 <= 6:
        print("El valor del programa sigue siendo de $",base)
    
    option3 = float(input("Digite su último valor de pension del colegio: "))

    #Se hace el incremento sumando la cifra que resulte de la multiplicación de la base por el 15%

    if option3 >= 438901.5:
        incremento = base * 0.15
        base = base + incremento
        print("Ya que su último valor de pension del colegio es superior a $438901.5. El valor del programa tendrá un incremento de $",incremento,", su valor final es de $", base)
    
    elif option3 < 438901.5 and option3 > 0:
        print("El valor del programa sigue siendo de $",base)

    option4 = float(input("Digite el patrimonio de su familia: "))

        #Se hace el incremento sumando la cifra que resulte de la multiplicación de la base por el 1.5%

    if option4 >= 200000000:
        incremento = option4 * 0.015
        base = base + incremento
        print("Ya que su patrimonio es mayor a $200.000.000, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",base)

    elif option4 < 200000000 and option4 > 0:
        print("El valor del programa sigue siendo de $",base)

    option5 = int(input("Por favor digite su edad: "))

    if option5 >= 18:
        base = base - 50000
        print("Por pandemia al ser mayor de edad tendrá un decuento de $50.000. Su valor toal es $",base)

    elif option5 < 18:
        base = base - 100000
        print("Por pandemia al ser menor de edad tendrá un decuento de $100.000. Su valor toal es $",base)

if option == 2:
    base = 2300000
    print("El programa de ingeniería electronica tiene un costo de $",base)

    option2 = int(input("Elija su estrato: |1|2|3|4|5|6|: "))

    if option2 >= 1 and option2 <= 3:

        descuento = base*0.05
        base = base - descuento
        print("Ya que su estrato esta entre 1 y 3 obtendra un descuento de $",descuento,". Su valor total seria de $",base)
    
    elif option2 >= 4 and option2 <= 6:
        print("El valor del programa sigue siendo de $",base)
    
    option3 = float(input("Digite su último valor de pension del colegio: "))
    
    if option3 >= 438901.5:
        incremento = base * 0.15
        base = base + incremento
        print("Ya que su último valor de pension del colegio es superior a $438901.5. El valor del programa tendrá un incremento de $",incremento,", su valor final es de $", base)
    
    elif option3 < 438901.5 and option3 > 0:
        print("El valor del programa sigue siendo de $",base)

    option4 = float(input("Digite el patrimonio de su familia: "))

    if option4 >= 200000000:
        incremento = option4 * 0.015
        base = base + incremento
        print("Ya que su patrimonio es mayor a $200.000.000, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",base)

    elif option4 < 200000000 and option4 > 0:
        print("El valor del programa sigue siendo de $",base)

    option5 = int(input("Por favor digite su edad: "))

    if option5 >= 18:
        base = base - 50000
        print("Por pandemia al ser mayor de edad tendrá un decuento de $50.000. Su valor toal es $",base)

    elif option5 < 18:
        base = base - 100000
        print("Por pandemia al ser menor de edad tendrá un decuento de $100.000. Su valor toal es $",base)

if option == 3:
    base = 4500000
    print("El programa de ingeniería mecatrónica tiene un costo de $",base)

    option2 = int(input("Elija su estrato: |1|2|3|4|5|6|: "))

    if option2 >= 1 and option2 <= 3:

        descuento = base*0.05
        base = base - descuento
        print("Ya que su estrato esta entre 1 y 3 obtendra un descuento de $",descuento,". Su valor total seria de $",base)
    
    elif option2 >= 4 and option2 <= 6:
        print("El valor del programa sigue siendo de $",base)
    
    option3 = float(input("Digite su último valor de pension del colegio: "))
    
    if option3 >= 438901.5:
        incremento = base * 0.15
        base = base + incremento
        print("Ya que su último valor de pension del colegio es superior a $438901.5. El valor del programa tendrá un incremento de $",incremento,", su valor final es de $", base)
    
    elif option3 < 438901.5 and option3 > 0:
        print("El valor del programa sigue siendo de $",base)

    option4 = float(input("Digite el patrimonio de su familia: "))

    if option4 >= 200000000:
        incremento = option4 * 0.015
        base = base + incremento
        print("Ya que su patrimonio es mayor a $200.000.000, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",base)

    elif option4 < 200000000 and option4 > 0:
        print("El valor del programa sigue siendo de $",base)

    option5 = int(input("Por favor digite su edad: "))

    if option5 >= 18:
        base = base - 50000
        print("Por pandemia al ser mayor de edad tendrá un decuento de $50.000. Su valor toal es $",base)

    elif option5 < 18:
        base = base - 100000
        print("Por pandemia al ser menor de edad tendrá un decuento de $100.000. Su valor toal es $",base) 

if option == 4:
    base = 3500000
    print("El programa de ingeniería electronica tiene un costo de $",base)

    option2 = int(input("Elija su estrato: |1|2|3|4|5|6|: "))

    if option2 >= 1 and option2 <= 3:

        descuento = base*0.05
        base = base - descuento
        print("Ya que su estrato esta entre 1 y 3 obtendra un descuento de $",descuento,". Su valor total seria de $",base)
    
    elif option2 >= 4 and option2 <= 6:
        print("El valor del programa sigue siendo de $",base)
    
    option3 = float(input("Digite su último valor de pension del colegio: "))
    
    if option3 >= 438901.5:
        incremento = base * 0.15
        base = base + incremento
        print("Ya que su último valor de pension del colegio es superior a $438901.5. El valor del programa tendrá un incremento de $",incremento,", su valor final es de $", base)
    
    elif option3 < 438901.5 and option3 > 0:
        print("El valor del programa sigue siendo de $",base)

    option4 = float(input("Digite el patrimonio de su familia: "))

    if option4 >= 200000000:
        incremento = option4 * 0.015
        base = base + incremento
        print("Ya que su patrimonio es mayor a $200.000.000, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",base)

    elif option4 < 200000000 and option4 > 0:
        print("El valor del programa sigue siendo de $",base)

    option5 = int(input("Por favor digite su edad: "))

    if option5 >= 18:
        base = base - 50000
        print("Por pandemia al ser mayor de edad tendrá un decuento de $50.000. Su valor toal es $",base)

    elif option5 < 18:
        base = base - 100000
        print("Por pandemia al ser menor de edad tendrá un decuento de $100.000. Su valor toal es $",base) 

else:
    print("Esta opción es incorrecta")

    
   


    
    
