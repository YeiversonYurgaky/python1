#Yeiverson Yurgaky Jimenez

class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKCYAN = '\033[96m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

import math

print(bcolors.OKCYAN + "►►►Calculadora Trigonométrica◄◄◄" + bcolors.ENDC)

while True:

    print(bcolors.HEADER + """
    ¿Que serie desea evaluar?
     1. Exponencial 
     2. Logaritmo natural 
     3. Logaritmo decimal 
     4. Funciones Trigonométricas
    """  + bcolors.ENDC)
    serie = int(input(bcolors.BOLD + "Serie: " + bcolors.ENDC))

    if serie == 1:
        #Exponencial

        exponencial_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if exponencial_x >= 0:

            sumatoria = 0

            for rango_n in range(0,10,1):
                factorial_n = 1
                for calculo in range(1,rango_n+1,1):
                    factorial_n = factorial_n * calculo

                exponencial = pow(exponencial_x,rango_n)/factorial_n
                sumatoria = sumatoria + exponencial

            print(bcolors.OKGREEN + f"El exponecial de {exponencial_x} segpun las serie de Maclaurin es {sumatoria:.4} y según python es {math.exp(exponencial_x):.4}" + bcolors.ENDC)

    elif serie == 2:
        logn_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if logn_x > 0:
            
            sumatoria = 0

            for n in range(10):

                logn = 2 * (1 / (2*n+1)) * ((logn_x-1) / (logn_x+1) ** (2*n+1))
                sumatoria = sumatoria + logn

            print(bcolors.OKGREEN + f"El logaritmo natural de {logn_x} según las series de Maclaurin es {sumatoria:.3}, y según python es {math.log(logn_x):.3}" + bcolors.ENDC)

    elif serie == 3:
        logd_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if logd_x > 0:
            sumatoria = 0

            for n in range(10):
                logn = 2 * (1 / (2*n+1)) * ((logd_x-1) / (logd_x+1) ** (2*n+1))
                sumatoria = sumatoria + logn

            log_deci = sumatoria / 2.30259
 
            print(bcolors.OKGREEN + f"El logaritmo decimal de {logd_x} según las series de Maclaurin es {log_deci:.3}, y según python es {math.log(logd_x) / 2.30259:.3}" + bcolors.ENDC)

    elif serie == 4:
        print(bcolors.HEADER + "¿Que serie desea evaluar? | 1. Seno | 2. Coseno | 3. Tangente | 4. Cosecante | 5. Secante | 6. Contangente |: " + bcolors.ENDC)

        funcion = int(input(bcolors.BOLD + "Elija una opción: " + bcolors.ENDC))

        if funcion < 1 or funcion > 6:
            print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)

        else:

            option2 = int(input(bcolors.HEADER + "Como desea digitar su angulo | 1. En grados | 2. En radianes |: " + bcolors.ENDC))

            #Converción de grados a radianes
            if option2 == 1: 
                angulo = float(input(bcolors.BOLD + "Digite el ángulo en grados: " + bcolors.ENDC))

                radianes = angulo*math.pi/180

            elif option2 == 2:

                radianes = float(input("Digite el ángulo en radianes: "))

            else:

                print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)

            if funcion == 1:
                                
                            #Seno

                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                if option2 == 1:                                #Depende de la elección del usuario la respuesta será personalizada
                    print(bcolors.OKGREEN + f"el seno de {convercion} grados es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.sin(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"el seno de {radianes} radianes es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.sin(radianes):.3f}" + bcolors.ENDC)

            elif funcion == 2:

                        #coseno

                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2*rango_n

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n) * pow(radianes,2*rango_n) / factorial_n #esta es la serie del coseno
                    sumatoria = sumatoria + coseno #la sumatoria de la serie del coseno
                                
                if option2 == 1:                        #Depende de la elección del usuario la respuesta será personalizada
                    print(bcolors.OKGREEN + f"el coseno de {convercion} grados es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"el coseno de {radianes} radianes es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes):.3f}" + bcolors.ENDC)

            elif funcion == 3:

                                    #tangente = seno/coseno

                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                sumatoria2 = 0

                for rango_n2 in range(0,10,1):

                    factorial_n2 = 1
                    denominador2 = 2*rango_n2

                    for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                        factorial_n2 = factorial_n2 * calculo2

                    convercion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                    sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno

                tangente = sumatoria / sumatoria2 

                if option2  == 1:
                    print(bcolors.OKGREEN + f"la tangente de {convercion:.1f} grados es: {tangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"la tangente de {radianes} radianes es: {tangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes):.3f}" + bcolors.ENDC)

            elif funcion == 4:

                                #COSECANTE

                                #cotangente = coseno/seno    


                                #coseno
                sumatoria2 = 0

                for rango_n2 in range(0,10,1):

                    factorial_n2 = 1
                    denominador2 = 2*rango_n2

                    for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                        factorial_n2 = factorial_n2 * calculo2

                    convercion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                    sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno
                
                                    #seno
                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                cotangente = sumatoria2 / sumatoria

                cosecante = cotangente/sumatoria2

                if option2  == 1:
                    print(bcolors.OKGREEN + f"la tangente de {convercion2} grados es: {cosecante:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes)/math.sin(radianes)/math.cos(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"la tangente de {radianes} radianes es: {cosecante:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes)/math.sin(radianes)/math.cos(radianes):.3f}" + bcolors.ENDC)

            elif funcion == 5:
                                    #Secante = tangente/seno
                                
                                    #tangente = seno/coseno

                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                sumatoria2 = 0

                for rango_n2 in range(0,10,1):

                    factorial_n2 = 1
                    denominador2 = 2*rango_n2

                    for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                        factorial_n2 = factorial_n2 * calculo2

                    convercion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                    sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno

                tangente = sumatoria / sumatoria2

                secante = tangente / sumatoria

                if option2  == 1:
                    print(bcolors.OKGREEN + f"la tangente de {convercion2} grados es: {secante:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes) / math.sin(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"la tangente de {radianes} radianes es: {secante:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes) / math.sin(radianes):.3f}" + bcolors.ENDC)

            elif funcion == 6:
                                #cotangente = coseno/seno    


                                #coseno
                sumatoria2 = 0

                for rango_n2 in range(0,10,1):

                    factorial_n2 = 1
                    denominador2 = 2*rango_n2

                    for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                        factorial_n2 = factorial_n2 * calculo2

                    convercion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                    sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno
                
                                    #seno
                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    convercion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                cotangente = sumatoria2 / sumatoria

                if option2  == 1:
                    print(bcolors.OKGREEN + f"la tangente de {convercion} grados es: {cotangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes)/math.sin(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"la tangente de {radianes} radianes es: {cotangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes)/math.sin(radianes):.3f}" + bcolors.ENDC)
        

    else:
    
        print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)
                

    


















    respuesta = str(input(bcolors.WARNING + "¿Desea seguir usando la calculadora? si/no: " + bcolors.ENDC))
    if respuesta == "no":
        break   
