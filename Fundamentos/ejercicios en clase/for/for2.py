"""
9.	Hacer algoritmo que lea
 un número y muestre su factorial.


n = int(input("Digite un numero entero: "))

f = 1 #1 modulo de multiplicaiónn

for i in range(1,n+1):  #n+1 porqué incloye n
    f = f * i
print(f)
"""














"""
10.	Hacer algoritmo que lea dos números N1
 y N2 donde N2 > N1. Calcular y mostrar el factorial de todos los números 
 comprendidos entre N1 y N2 incluyéndolos
"""
import math

n1 = int(input("Digite el primer número: "))
n2 = int(input("Digite el segundo número: "))

for i in range(n1,n2+1,1):

    f = 1
    
    for j in range(1,i+1):

        f = f * j
    
print(i, f)


"""
n1 = int(input("Digite el primer número que debe ser menor que el segundo: "))

n2 = int(input("Digite el segundo número: "))

f = 1

for i in range(1,n1+1):

    f = f * i

print(f"El factorial de {n1} es {f}")



for i in range(n1+1, n2+1):

    f = f*i

    print(f"El factorial de {i} es {f}")
"""
"""
11.	El número de combinaciones de m elementos,
 tomados en grupos de n elementos, viene dado por la fórmula C = m!/(n!*(m-n)!. Ha
algoritmo que lea m y n y calcule y muestre C.
"""

m = int(input("Digite el número de combinaciones: "))
n1 = int(input("Digite el numero de grupos: "))


