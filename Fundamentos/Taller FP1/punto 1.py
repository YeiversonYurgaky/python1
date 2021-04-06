print("Programas de la Universidad de Innovación de Medellín")

option = int(input("Elija el progrma que desea cursar: |1. Ingeniería de sistemas|2. Ingeniería electronica|3. Ingeniería mecatrónica|4. Ingeniería de sistemas complejos: "))

if option == 1:
    base = 2000000
    print("El programa de ingeniería de sistemas tiene un costo de $",base)
    option2 = int(input("Elija su estrato: |1|2|3|4|5|6|: "))

    if option2 >= 1 and option2 <= 3:
        descuento = base*0.05
        preciofinal = base - descuento
        print("Ya que su estrato esta entre 1 y 3 obtendra un descuento de $",descuento,". Su valor total seria de $",preciofinal)

        pension = float(input("Por favor digite su último valor de pension del colegio: "))
        
        if pension > 438901:
            incremento = preciofinal*0.15
            preciofinal = preciofinal + incremento
            print("Ya que su último valor de pensión supera la mitad del sario minimo el año 2020, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",preciofinal) 

            patrimonio = float(input("Por favor digite el patrimonio de su familia: "))

            if patrimonio > 200000000:
                incremento = preciofinal * 0.015
                preciofinal = preciofinal + incremento
                print("Ya que su patrimonio es mayor a $200.000.000, el precio del programa tendra un incremento de $",incremento,". Su valor totas seria de $",preciofinal)
       
                edad = int(input("Por favor digite su edad: "))

                if edad < 18:
                    preciofinal = preciofinal - 100000
                    print("Por pandemia al ser menor de edad tendrá un decuento de $100.000. Su valor total es $",preciofinal)

                else:
                    preciofinal = preciofinal - 50000
                    print("Por pandemia al ser mayor de edad tendrá un decuento de $50.000. Su valor toal es $",preciofinal)

            else:
                print("Ya que su patrimonio es menor a $200.000.000 el programa tendrá un valor de",preciofinal)
        


   
     





    
    

    

    
