'''
las listas son estructuras de datos que se usan para almacenar valores.
Se asemejan a los vectores

Append(<obj>)
    Este método nos permite agregar nuevos elementos a una lista/vector.

Remove(<indice>)
    El método remove va a remover un elemento que se le pase como
    parámentro de la lista a donde se le esté aplicando.

Index(<dato>)
    Index devuelve el número de indice del elemento que le pasemos por parámetro.

Count(<dato>)
    Para saber cuántas veces un elemento de una lista
    se repite podemos utilizar el metodo count().

Reverse()
    También podemos invertir los elementos  de una lista.
'''

def main() :
     ''' Escriba un programa que pida dos números enteros y escriba qué
    números son pares y cuáles impares desde el primero hasta el segundo.

     num1 = int(input("Primero: "))
     num2 = int(input("Segundo: "))

     pares = []
     impares = []

     for i in range(num1,num2):

        if i %2 == 0:
            pares.append(i)

        else: impares.append(i)

     print("pares: ",pares)
     print("impares: ",impares)
'''
    
     #lista = [1,2,3,4,5,6,7,8,9]
     #print(lista[0])
     #lista = [1,2,3,4,5,6,7,8,9]
     #lista.remove(4)
     #print(lista)
     #lista = [1,2,3,4,5,6,7,8,9]
     #print(lista.index(5))
     lista = [1,2,3,4,5,6,7,8,9]
     lista.reverse()
     print(lista)



main()