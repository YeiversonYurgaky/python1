#Yeiverson Yurgaky Jimenez

print("→→Conversiones de longitud, masa y volumen←←")

option = int(input("Elija una opción: 1. Longitud, 2. Masa, 3. Volumen: "))

if option == 1:
    option2 = int(input("Elija una opción: 1. De metros a kilometros, 2. De millas a pies, 3. De pulgadas a centimetros: "))

   #Usamos las formulas existentes para hacer la conversión de longitudes, cada formula con su respectiva variable. 

    if option2 == 1:
        metros = float(input("Digite el valor a convertir: "))
        if  metros < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            kilometros = metros*(1.0/1000)
            print("El valor de "+str(metros),"metros es igual a "+str(kilometros),"kilometros")
        
    elif option2 == 2:
        millas = float(input("Digite el valor a convertir: "))
        if millas < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            pies = millas*(5.280/1.10)
            print("El valor de "+str(millas),"millas es igual a "+str(pies),"pies")

    elif option2 == 3:
        pulgadas = float(input("Digite el valor a convertir: "))
        if pulgadas < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            centimetros = pulgadas*2.54
            print("El valor de "+str(pulgadas),"pulgadas es igual a "+str(centimetros),"centimetros")

    else:
        print("Ha digitado una opción incorrecta")

elif option == 2:
    option2 = int(input("Elija una opción: 1. Kilogramos a libras, 2. Onzas a gramos, 3. Toneladas a kilogramos: "))

 #Usamos las formulas existentes para hacer la conversión de la masa, cada formula con su respectiva variable.

    if option2 == 1:
        kilogramos = float(input("Dijite el valor a convertir: "))
        if kilogramos < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            libras = kilogramos*(2.2046/1.0)
            print("El valor de "+str(kilogramos),"kilogramos es igual a "+str(libras),"libras")

    elif option2 == 2:
        onzas = float(input("Dijite el valor a convertir: "))
        if onzas < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            gramos = onzas*(28.3495/1.0)  
            print("El valor de "+str(onzas),"onzas es igual a "+str(gramos),"gramos")    

    elif option2 == 3:
        toneladas = float(input("Dijite el valor a convertir: "))
        if toneladas < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            kilogramos = toneladas*(1000/1)
            print("El valor de "+str(toneladas),"toneladas es igual a "+str(kilogramos),"kilogramos")         

    else:
        print("Ha digitado una opción incorrecta")        

elif option == 3:
    option2 = int(input("Elija una opción: 1. Metros cúbicos a litros, 2. Litros a metros cúbicos: "))

 #Usamos las formulas existentes para hacer la conversión del volumen, cada formula con su respectiva variable.

    if option2 == 1:
        metroscubi = float(input("Digite el valor a convertir: "))
        if metroscubi < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:    
            litros = metroscubi*(1000/1)
            print("El valor de "+str(metroscubi),"metros cúbicos es igual a "+str(litros),"litros")

    elif option2 == 2:
        litros = float(input("Digite el valor a convertir: "))
        if litros < 0:
            print("No puedes digitar un valor negativo. Intenta nuevamente")
        else:
            metroscubi = litros*(1/1000)
            print("El valor de "+str(litros),"litros es igual a "+str(metroscubi),"metros cúbicos")
    
    else:
        print("Ha digitado una opción incorrecta")

else:
     print("Lo siento, esa opción no existe")




