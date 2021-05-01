'''
Crea un array de 10 posiciones de números aleatorios.  Muestra por consola el indice y el valor al que corresponde.

lista = [1,2,3,4,5,6,7,8,9,10,11]
print(f"El indice del valor {lista[7]} es {lista.index(8)}")
'''
'''Crea un array de números de un tamaño pasado por teclado, 
el array contendrá números aleatorios impares entre los números deseados, 
por último nos indica cual es el mayor de todos.'''

def main():

    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    impares = []
    impares2 = []

    for i in range(num1,num2+1):

        if i %2 != 0:
            impares.append(i)
    print("impares: ",impares)

    for j in range(num1,num2+1):

        if j %2 != 0:
            impares2.append(j)
            impares2.reverse()
    print("El mayor es el",impares2[0])
main()
'''
Crea un array de números de 100 posiciones, que contendrá los números del 
1 al 100. Obtén la suma de todos ellos y el promedio. 

    promedio = suma(elementos)/elementos

lista = []
suma = 0
for i in range(1,101):
    lista.append(i)
    suma = suma + i
    promedio = suma / 100
print(promedio)
'''

'''Realizar un programa que muestre por pantalla la traspuesta de una matriz

matriz = [
         [1,2,3],
         [4,5,6]
         ]
traspuesta = [
             [1,4],
             [2,5],
             [3,6]
             ]
print("Matriz", matriz)
print("Matriz traspuesta",traspuesta)
'''
