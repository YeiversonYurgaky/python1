#Yeiverson Yurgaky Jimenez

class bcolors: #para darle colores a las letras al iniciar el programa

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKCYAN = '\033[96m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'
import math #para poder usar diferentes comando para hacer calculos según los métodos de python
import os #para poder limpiar pantalla


print(bcolors.OKCYAN + "►►►Calculadora Trigonométrica◄◄◄" + bcolors.ENDC)

while True: #controlador de flujo

    print(bcolors.HEADER + """
    ¿Que serie desea evaluar?
     1. Exponencial 
     2. Logaritmo natural 
     3. Logaritmo decimal 
     4. Funciones Trigonométricas
    """  + bcolors.ENDC)

    serie = int(input(bcolors.BOLD + "Serie: " + bcolors.ENDC))
    
    #exponencial
    
    if serie == 1:
        #Exponencial

        exponencial_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if exponencial_x >= 0:

            sumatoria = 0

            for rango_n in range(0,10,1):
                factorial_n = 1
                for calculo in range(1,rango_n+1,1):   
                    factorial_n = factorial_n * calculo #Se le saca el factorial 

                exponencial = pow(exponencial_x,rango_n)/factorial_n #Serie del exponencial
                sumatoria = sumatoria + exponencial     #Sumatoria funciona como acumulador

            print(bcolors.OKGREEN + f"El exponecial de {exponencial_x} segpun las serie de Maclaurin es {sumatoria:.4} y según python es {math.exp(exponencial_x):.4}" + bcolors.ENDC)

        else:
            print(bcolors.FAIL + "El valor de x no puede ser negativo" + bcolors.ENDC)
   
    #logaritmo natural
   
    elif serie == 2:
        logn_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if logn_x > 0:
            
            sumatoria = 0

            for rango_n in range(10):

                logn = 2 * (1 / (2*rango_n+1)) * ((logn_x-1) / (logn_x+1) ** (2*rango_n+1)) #serie del logaritmo natural
                sumatoria = sumatoria + logn    #se acumula el valor de logn

            print(bcolors.OKGREEN + f"El logaritmo natural de {logn_x} según las series de Maclaurin es {sumatoria:.3}, y según python es {math.log(logn_x):.3}" + bcolors.ENDC)

        else:
            print(bcolors.FAIL + "El logaritmo natural no se puede calcular con números negativos" + bcolors.ENDC)
    
    #logaritmo decimal
    
    elif serie == 3:
        logd_x = float(input(bcolors.BOLD + "Digite el valor de x: " + bcolors.ENDC))

        if logd_x > 0:
            sumatoria = 0

            for rango_n in range(10):
                logn = 2 * (1 / (2*rango_n+1)) * ((logd_x-1) / (logd_x+1) ** (2*rango_n+1)) #serie del logaritmo natural
                sumatoria = sumatoria + logn   #se acumula el valor de logn

            log_deci = sumatoria / 2.30259 #formula del logaritmo decimal
 
            print(bcolors.OKGREEN + f"El logaritmo decimal de {logd_x} según las series de Maclaurin es {log_deci:.3}, y según python es {math.log(logd_x) / 2.30259:.3}" + bcolors.ENDC)

        else:
            print(bcolors.FAIL + "El logaritmo decimal no se puede calcular con números negativos" + bcolors.ENDC)

    #funciones trigonométricas

    elif serie == 4:
        print(bcolors.HEADER + """
         ¿Que serie desea evaluar? 
         1. Seno
         2. Coseno 
         3. Tangente 
         4. Cosecante 
         5. Secante  
         6. Contangente""" + bcolors.ENDC)


        funcion = int(input(bcolors.BOLD + "Elija una opción: " + bcolors.ENDC))

        if funcion < 1 or funcion > 6:
            print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)

        else:

            option2 = int(input(bcolors.HEADER + "Como desea digitar su angulo | 1. En grados | 2. En radianes |: " + bcolors.ENDC))

            #Conversión de grados a radianes
            if option2 == 1: 
                angulo = float(input(bcolors.BOLD + "Digite el ángulo en grados: " + bcolors.ENDC))

                radianes = angulo*math.pi/180

            elif option2 == 2:

                radianes = float(input("Digite el ángulo en radianes: "))

            else:           
                print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)
            
            #Seno
            
            if funcion == 1:
                                
                            

                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2 * rango_n + 1

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                    sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                if option2 == 1:                                #Depende de la elección del usuario la respuesta será personalizada
                    print(bcolors.OKGREEN + f"el seno de {conversion} grados es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.sin(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"el seno de {radianes} radianes es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.sin(radianes):.3f}" + bcolors.ENDC)

            #Coseno

            elif funcion == 2:



                sumatoria = 0

                for rango_n in range(0,10,1):

                    factorial_n = 1
                    denominador = 2*rango_n

                    for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                        factorial_n = factorial_n * calculo

                    conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                    coseno = pow(-1,rango_n) * pow(radianes,2*rango_n) / factorial_n #esta es la serie del coseno
                    sumatoria = sumatoria + coseno #la sumatoria de la serie del coseno
                                
                if option2 == 1:                        #Depende de la elección del usuario la respuesta será personalizada
                    print(bcolors.OKGREEN + f"el coseno de {conversion} grados es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes):.3f}" + bcolors.ENDC)

                else:
                    print(bcolors.OKGREEN + f"el coseno de {radianes} radianes es: {sumatoria:.3f} según la serie de McLaurin, y según los métodos de python es de {math.cos(radianes):.3f}" + bcolors.ENDC)

            #Tangente = seno/coseno

            elif funcion == 3:

                if radianes == (math.pi/2):     #tenemos en cuenta la regla de la tangente
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la tangente de π/2 o 90° da indeterminado" + bcolors.ENDC)
                    

                                    
                else:
                                        #seno
                    sumatoria = 0

                    for rango_n in range(0,10,1):

                        factorial_n = 1
                        denominador = 2 * rango_n + 1

                        for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                            factorial_n = factorial_n * calculo

                        conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                        sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                                        #coseno

                    sumatoria2 = 0

                    for rango_n2 in range(0,10,1):

                        factorial_n2 = 1
                        denominador2 = 2*rango_n2

                        for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                            factorial_n2 = factorial_n2 * calculo2

                        conversion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                        sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno

                    tangente = sumatoria / sumatoria2  #tangente es igual a la sumatoria del seno sobre la sumatoria del coseno

                    if option2  == 1:                                 #Depende de la elección del usuario la respuesta será personalizada
                        print(bcolors.OKGREEN + f"la tangente de {conversion:.1f} grados es: {tangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes):.3f}" + bcolors.ENDC)

                    else:
                        print(bcolors.OKGREEN + f"la tangente de {radianes} radianes es: {tangente:.3f} según la serie de McLaurin, y según los métodos de python es de {math.tan(radianes):.3f}" + bcolors.ENDC)

            #Cosecante = 1/seno

            elif funcion == 4:

                if radianes == 0:   #tenemos en cuenta las reglas del cosecante
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la cosecante de o da indeterminado" + bcolors.ENDC)

                elif radianes == (math.pi):
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la cosecante de π o 180° da indeterminado" + bcolors.ENDC)

                                
    
                else:
                                        #seno
                    sumatoria = 0

                    for rango_n in range(0,10,1):

                        factorial_n = 1
                        denominador = 2 * rango_n + 1

                        for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                            factorial_n = factorial_n * calculo

                        conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                        sumatoria = sumatoria + seno            #la sumatoria de la serie del seno


                    cosecante = 1/sumatoria #cosecante es igual a 1 sobre la sumatoria del seno

                    if option2  == 1:                               #Depende de la elección del usuario la respuesta será personalizada
                        print(bcolors.OKGREEN + f"la cosecante de {conversion} grados es: {cosecante:.3f} según la serie de McLaurin, y según los métodos de python es de {1/math.sin(radianes):.3f}" + bcolors.ENDC)

                    else:
                        print(bcolors.OKGREEN + f"la cosecante de {radianes} radianes es: {cosecante:.3f} según la serie de McLaurin, y según los métodos de python es de {1/math.sin(radianes):.3f}" + bcolors.ENDC)

            #Secante = 1/coseno

            elif funcion == 5:

                if radianes == (math.pi/2):     #tenemos en cuenta la regla de la secante
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la secante de π/2 o 90° da indeterminado" + bcolors.ENDC)
                                    
                                
                else:

                        #coseno

                    sumatoria = 0

                    for rango_n in range(0,10,1):

                        factorial_n = 1
                        denominador = 2*rango_n

                        for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                            factorial_n = factorial_n * calculo

                        conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        coseno = pow(-1,rango_n) * pow(radianes,2*rango_n) / factorial_n #esta es la serie del coseno
                        sumatoria = sumatoria + coseno #la sumatoria de la serie del coseno

                    secante = 1 / sumatoria  #secante es igual a 1 sobre la sumatoria del coseno

                    if option2  == 1:                               #Depende de la elección del usuario la respuesta será personalizada
                        print(bcolors.OKGREEN + f"la secante de {conversion} grados es: {secante:.3f} según la serie de McLaurin, y según los métodos de python es de {1 / math.cos(radianes):.3f}" + bcolors.ENDC)

                    else:
                        print(bcolors.OKGREEN + f"la secante de {radianes} radianes es: {secante:.3f} según la serie de McLaurin, y según los métodos de python es de {1 / math.cos(radianes):.3f}" + bcolors.ENDC)

            #cotangente = 1/tangente

            elif funcion == 6:

                if radianes == 0:   #tenemos en cuenta las reglas de la cotangente
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la cotangente de o da indeterminado" + bcolors.ENDC)

                elif radianes == (math.pi):
                    print(bcolors.FAIL + "No puede ingresar este valor, ya que la cotangente de π o 180° da indeterminado" + bcolors.ENDC)
                            
                                    

                                    #tangente = seno/coseno
                else:
                                    #seno
                    sumatoria = 0

                    for rango_n in range(0,10,1):

                        factorial_n = 1
                        denominador = 2 * rango_n + 1

                        for calculo in range(1,denominador+1,1):  #se calcula el factorial del denominador
                            factorial_n = factorial_n * calculo

                        conversion = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        seno = pow(-1,rango_n) * pow(radianes,2*rango_n+1) / factorial_n        #esta es la serie del seno
                        sumatoria = sumatoria + seno            #la sumatoria de la serie del seno

                                    #coseno

                    sumatoria2 = 0

                    for rango_n2 in range(0,10,1):

                        factorial_n2 = 1
                        denominador2 = 2*rango_n2

                        for calculo2 in range(1,denominador2+1,1):  #se calcula el factorial del denominador
                            factorial_n2 = factorial_n2 * calculo2

                        conversion2 = math.degrees(radianes) #cambiamos los radiades a grados de nuevo, para cuando el usuario ingrese el valor en grados darle la respuesa en grados
                        coseno = pow(-1,rango_n2) * pow(radianes,2*rango_n2) / factorial_n2 #esta es la serie del coseno
                        sumatoria2 = sumatoria2 + coseno #la sumatoria de la serie del coseno

                    tangente = sumatoria / sumatoria2 #tangente es igual a la sumatoria del seno sobre la sumatoria del coseno
                    cotangente = 1 / tangente         #cotangente es igual a 1 sobre la sumatoria de la tangente

                    if option2  == 1:                                  #Depende de la elección del usuario la respuesta será personalizada
                        print(bcolors.OKGREEN + f"la cotangente de {conversion} grados es: {cotangente:.3f} según la serie de McLaurin, y según los métodos de python es de {1/math.tan(radianes):.3f}" + bcolors.ENDC)

                    else:
                        print(bcolors.OKGREEN + f"la cotangente de {radianes} radianes es: {cotangente:.3f} según la serie de McLaurin, y según los métodos de python es de {1/math.tan(radianes):.3f}" + bcolors.ENDC)
        
    else:
    
        print(bcolors.FAIL + "La opción digitada no existe" + bcolors.ENDC)
                
    respuesta = str(input(bcolors.WARNING + "¿Desea seguir usando la calculadora? | 1. Si | 2. No |: " + bcolors.ENDC)) #controlador de flujo
    if respuesta == "2":
        os.system("cls") #para poder limpiar pantalla
        break  
    else:
        os.system("cls") #para poder limpiar pantalla
