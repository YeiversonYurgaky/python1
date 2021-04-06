"""
Diseñar un algoritmo que escriba la equivalencia cualitativa de una nota numérica leída y 
que muestre si aprobó o no. Una nota aprobatoria vale 3 en adelante.
Escala numérica
Escala Cualitativa
[4.6, 5.0]
Excelente
[4.1, 4.5]
Muy bueno
[3.6, 4.0]
Bueno
[3.3, 3.5]
Aceptable
[3.0, 3.2]
Aprobado
[2.6, 2.9]
Deficiente
[2.1, 2.5]
Malo
[0.0, 2.0]
Por mejorar considerablemente
"""
nota=float(input("Digite su nota: "))
if nota>= 4.6 and nota<=5.0:
    print("Exelente: "+str(nota))
if nota>=4.1 and nota<=4.5:
    print("Muy bueno: "+str(nota))
if nota>=3.6 and nota<=4.0:
    print("Bueno: "+str(nota))
if nota>=3.3 and nota<=3.5:
    print("Aceptable: "+str(nota))
if nota>=3.0 and nota<=3.2:
    print("Aprobado: "+str(nota))
if nota>=2.6 and nota<=2.9:
    print("Deficiente: "+str(nota))
if nota>= 2.1 and nota<=2.5:
    print("Malo: "+str(nota))
if nota>= 0.0 and nota<= 2.0:
    print("Por mejorar considerablemente: "+str(nota))
if nota>5.0:
    print("No puede digitar una nota mayor a 5.0")












    """
    Se requiere un algoritmo que le permita al usuario determinar si dadas dos funciones, se intersectan en un 
    valor de X dado por él. Las Funciones son: F1(x) = x y F2(x) = x2
"""

x=float(input("Digite el valor de x: "))

if x == pow(x,2):
    print("En ese valor de x las funciones se intersectan")
else:
    print("En ese valor de x las funciones no se intersectan")

